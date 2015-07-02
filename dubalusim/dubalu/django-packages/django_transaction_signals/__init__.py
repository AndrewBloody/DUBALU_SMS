# -*- coding: utf-8 -*-
#
# post_commit and post_rollback transaction signals for Django with monkey
# patching
#
# Author Grégoire Cachet <gregoire.cachet@gmail.com>
# http://gist.github.com/247844

import warnings

from django.db import transaction
from django.db.transaction import Error, DatabaseError, get_connection
from django.dispatch import Signal
from django.dispatch.dispatcher import _make_id

try:
    import thread
except ImportError:
    import dummy_thread as thread


class BadlyBehavedTransactionSignalHandlerError(Exception):
    '''
    Exception raised when a post_commit or post_rollback handler updates the
    current transaction and doesn't perform its own commit/rollback. This is
    usually easily mitigated by using a wrapper like @commit_on_success.

    Also see the defer() function in this module for another approach that
    avoids this error.
    '''
    pass


class ThreadSignals(object):
    def __init__(self):
        self.post_commit = Signal()
        self.post_rollback = Signal()


class TransactionSignals(object):
    signals = {}

    def _has_signals(self):
        thread_ident = thread.get_ident()
        return thread_ident in self.signals

    def _init_signals(self):
        thread_ident = thread.get_ident()
        assert thread_ident not in self.signals
        self.signals[thread_ident] = ThreadSignals()
        return self.signals[thread_ident]

    def _remove_signals(self, savepoint_ids=None):
        thread_ident = thread.get_ident()
        assert thread_ident in self.signals
        if savepoint_ids is None:
            del self.signals[thread_ident]
        else:
            signals = self.signals[thread_ident]
            all_signals = []
            keep_signals = False
            for signal_type in ('post_commit', 'post_rollback'):
                for signal in getattr(signals, signal_type).receivers:
                    dispatch_uid = signal[0][0]
                    assert isinstance(dispatch_uid, tuple), "dispatch_uid for post_commit and post_rollback must be a tuple with the first elemebt being the savepoint_id"
                    keep = dispatch_uid[0] is None or dispatch_uid[0] in savepoint_ids
                    if keep:
                        keep_signals = True
                    all_signals.append((signal_type, dispatch_uid, keep))
            if keep_signals:
                for signal_type, dispatch_uid, keep in all_signals:
                    if not keep:
                        getattr(signals, signal_type).disconnect(dispatch_uid=dispatch_uid)
            else:
                del self.signals[thread_ident]

    def _get_signals(self):
        thread_ident = thread.get_ident()
        assert thread_ident in self.signals
        return self.signals[thread_ident]

    def _get_or_init_signals(self):
        if self._has_signals():
            return self._get_signals()
        else:
            return self._init_signals()

    def _send_post_commit(self, using=None):
        if self._has_signals():
            _signals = self._get_signals()
            self._remove_signals()

            _signals.post_commit.send(sender=transaction)

            # Take care of badly behaved signal handlers that have
            # dirtied the transaction without committing properly
            if transaction.is_dirty(using):
                raise BadlyBehavedTransactionSignalHandlerError

    def _send_post_rollback(self, using):
        if self._has_signals():
            _signals = self._get_signals()
            self._remove_signals()

            _signals.post_rollback.send(sender=transaction)

            # Take care of badly behaved signal handlers that have
            # dirtied the transaction without committing properly
            if transaction.is_dirty(using):
                raise BadlyBehavedTransactionSignalHandlerError

    def _on_exit_without_update(self, using):
        '''
        Clear signals on transaction exit, even if neither commit nor rollback
        happened.
        '''
        if self._has_signals():
            connection = get_connection(using)
            self._remove_signals(connection.savepoint_ids)

    @property
    def post_commit(self):
        return self._get_or_init_signals().post_commit

    @property
    def post_rollback(self):
        return self._get_or_init_signals().post_rollback


def apply_django_transaction_signals_patch():
    """
    Monkey patch django
    """
    if hasattr(transaction, '_django_transaction_signals_patch'):
        return

    NO_SIGNAL = 0
    COMMIT_SIGNAL = 1
    ROLLBACK_SIGNAL = 2
    SAVEPOINT_COMMIT_SIGNAL = 3
    SAVEPOINT_ROLLBACK_SIGNAL = 4

    # If post_commit or post_rollback signal handlers put the transaction in a
    # dirty state, they must handle their own commits/rollbacks.
    transaction.signals = TransactionSignals()

    def __exit__(self, exc_type, exc_value, traceback):
        # The following patch was applied to transaction.Atomic.__exit__
        # To django's 1.6 transaction (@475b3791a348002f99f9553e9baed67b75994701)

        signal = NO_SIGNAL

        connection = get_connection(self.using)

        if connection.savepoint_ids:
            sid = connection.savepoint_ids.pop()
        else:
            # Prematurely unset this flag to allow using commit or rollback.
            connection.in_atomic_block = False

        try:
            if connection.closed_in_transaction:
                # The database will perform a rollback by itself.
                # Wait until we exit the outermost block.
                pass

            elif exc_type is None and not connection.needs_rollback:
                if connection.in_atomic_block:
                    # Release savepoint if there is one
                    if sid is not None:
                        try:
                            connection.savepoint_commit(sid)
                            signal = SAVEPOINT_COMMIT_SIGNAL
                        except DatabaseError:
                            signal = SAVEPOINT_ROLLBACK_SIGNAL
                            try:
                                connection.savepoint_rollback(sid)
                            except Error:
                                # If rolling back to a savepoint fails, mark for
                                # rollback at a higher level and avoid shadowing
                                # the original exception.
                                connection.needs_rollback = True
                            raise
                else:
                    # Commit transaction
                    try:
                        connection.commit()
                        signal = COMMIT_SIGNAL
                    except DatabaseError:
                        signal = ROLLBACK_SIGNAL
                        try:
                            connection.rollback()
                        except Error:
                            # An error during rollback means that something
                            # went wrong with the connection. Drop it.
                            connection.close()
                        raise
            else:
                # This flag will be set to True again if there isn't a savepoint
                # allowing to perform the rollback at this level.
                connection.needs_rollback = False
                if connection.in_atomic_block:
                    # Roll back to savepoint if there is one, mark for rollback
                    # otherwise.
                    if sid is None:
                        connection.needs_rollback = True
                    else:
                        signal = SAVEPOINT_ROLLBACK_SIGNAL
                        try:
                            connection.savepoint_rollback(sid)
                        except Error:
                            # If rolling back to a savepoint fails, mark for
                            # rollback at a higher level and avoid shadowing
                            # the original exception.
                            connection.needs_rollback = True
                else:
                    # Roll back transaction
                    signal = ROLLBACK_SIGNAL
                    try:
                        connection.rollback()
                    except Error:
                        # An error during rollback means that something
                        # went wrong with the connection. Drop it.
                        connection.close()

        finally:
            # Outermost block exit when autocommit was enabled.
            if not connection.in_atomic_block:
                if connection.closed_in_transaction:
                    connection.connection = None
                elif connection.features.autocommits_when_autocommit_is_off:
                    connection.autocommit = True
                else:
                    connection.set_autocommit(True)
            # Outermost block exit when autocommit was disabled.
            elif not connection.savepoint_ids and not connection.commit_on_exit:
                if connection.closed_in_transaction:
                    connection.connection = None
                else:
                    connection.in_atomic_block = False

            if signal == COMMIT_SIGNAL:
                transaction.signals._send_post_commit(self.using)
            elif signal == ROLLBACK_SIGNAL:
                transaction.signals._send_post_rollback(self.using)
            elif signal == SAVEPOINT_ROLLBACK_SIGNAL:
                transaction.signals._on_exit_without_update(self.using)
            elif signal == NO_SIGNAL:
                transaction.signals._on_exit_without_update(self.using)

    transaction.Atomic.__exit__ = __exit__

    def commit_on_success(using=None):
        """
        This decorator activates commit on response. This way, if the view function
        runs successfully, a commit is made; if the viewfunc produces an exception,
        a rollback is made. This is one of the most common ways to do transaction
        control in Web apps.
        """
        warnings.warn("commit_on_success is deprecated in favor of atomic.",
            DeprecationWarning, stacklevel=2)

        def entering(using):
            transaction.enter_transaction_management(using=using)

        def exiting(exc_type, using):
            signal = NO_SIGNAL

            try:
                if exc_type is not None:
                    if transaction.is_dirty(using=using):
                        transaction.rollback(using=using)
                        signal = ROLLBACK_SIGNAL
                else:
                    signal = COMMIT_SIGNAL
                    if transaction.is_dirty(using=using):
                        try:
                            transaction.commit(using=using)
                        except:
                            transaction.rollback(using=using)
                            signal = ROLLBACK_SIGNAL
                            raise
            finally:
                transaction.leave_transaction_management(using=using)

                if signal == COMMIT_SIGNAL:
                    transaction.signals._send_post_commit(using)
                elif signal == ROLLBACK_SIGNAL:
                    transaction.signals._send_post_rollback(using)
                elif signal == SAVEPOINT_ROLLBACK_SIGNAL:
                    transaction.signals._on_exit_without_update(using)
                elif signal == NO_SIGNAL:
                    transaction.signals._on_exit_without_update(using)

        return transaction._transaction_func(entering, exiting, using)

    transaction.commit_on_success = commit_on_success

    transaction._django_transaction_signals_patch = True
apply_django_transaction_signals_patch()


def defer(f, *args, **kwargs):
    '''
    Wrapper that defers a function's execution until the current transaction
    commits, if a transaction is active.  Otherwise, executes as usual. Note
    that a deferred function will NOT be called if the transaction completes
    without committing (e.g. when transaction.is_dirty() is False upon exiting
    the transaction).

    An implicit assumption is that a deferred function does not return an
    important value, since there is no way to retrieve the return value in
    the normal execution order.

    Before being connected to the 'post_commit' signal of an existing managed
    transaction, the deferred function is wrapped by the @commit_on_success
    decorator to ensure that it behaves properly by committing or rolling back
    any updates it makes to a current transaction.

    >>> from django.db import transaction
    >>> from django_transaction_signals import defer
    >>>
    >>> def log_success(msg):
    >>>     print 'logging success'
    >>>
    >>> @transaction.atomic
    >>> def transactional_update(value):
    >>>     print 'starting transaction'
    >>>     defer(log_success, 'The transaction was successful')
    >>>     print 'finishing transaction'
    >>>
    >>> transactional_update('foo')
    ... starting transaction
    ... finishing transaction
    ... logging success

    '''
    connection = get_connection(kwargs.pop('using', None))
    if not connection.get_autocommit() or connection.in_atomic_block:
        def f_deferred(*a, **kw):
            f(*args, **kwargs)
        if connection.savepoint_ids:
            savepoint_id = connection.savepoint_ids[-1]
        else:
            savepoint_id = None
        dispatch_uid = (savepoint_id, _make_id(f_deferred))
        transaction.signals.post_commit.connect(f_deferred, weak=False, dispatch_uid=dispatch_uid)
    else:
        return f(*args, **kwargs)

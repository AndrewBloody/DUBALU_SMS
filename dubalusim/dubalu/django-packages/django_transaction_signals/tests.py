# -*- coding: utf-8 -*-
from django.test import TransactionTestCase

from django.db import transaction

from . import defer


class Failure(Exception):
    pass


class DeferTest(TransactionTestCase):
    def test_atomic_succeess(self):
        results = []
        try:
            with transaction.atomic():
                results.append('begins')
                defer(lambda *a, **kw: results.append('DEFERRED A'))
                try:
                    with transaction.atomic():
                        results.append('nested begins')
                        defer(lambda *a, **kw: results.append('DEFERRED NESTED'))
                        results.append('nested ends')
                except Failure:
                    pass
                defer(lambda *a, **kw: results.append('DEFERRED B'))
                results.append('ends')
        except Failure:
            pass
        self.failUnlessEqual(results, ['begins', 'nested begins', 'nested ends', 'ends', 'DEFERRED A', 'DEFERRED NESTED', 'DEFERRED B'], results)

    def test_atomic_nested_failure(self):
        results = []
        try:
            with transaction.atomic():
                results.append('begins')
                defer(lambda *a, **kw: results.append('DEFERRED A'))
                try:
                    with transaction.atomic():
                        results.append('nested begins')
                        defer(lambda *a, **kw: results.append('DEFERRED NESTED'))
                        results.append('nested ends')
                        raise Failure
                except Failure:
                    pass
                defer(lambda *a, **kw: results.append('DEFERRED B'))
                results.append('ends')
        except Failure:
            pass
        self.failUnlessEqual(results, ['begins', 'nested begins', 'nested ends', 'ends', 'DEFERRED A', 'DEFERRED B'], results)

    def test_atomic_failure(self):
        results = []
        try:
            with transaction.atomic():
                results.append('begins')
                defer(lambda *a, **kw: results.append('DEFERRED A'))
                try:
                    with transaction.atomic():
                        results.append('nested begins')
                        defer(lambda *a, **kw: results.append('DEFERRED NESTED'))
                        results.append('nested ends')
                except Failure:
                    pass
                defer(lambda *a, **kw: results.append('DEFERRED B'))
                results.append('ends')
                raise Failure
        except Failure:
            pass
        self.failUnlessEqual(results, ['begins', 'nested begins', 'nested ends', 'ends'], results)

    def test_commit_on_success_success(self):
        results = []
        try:
            with transaction.commit_on_success():
                results.append('begins')
                defer(lambda *a, **kw: results.append('DEFERRED A'))
                try:
                    with transaction.commit_on_success_unless_managed():
                        results.append('nested begins')
                        defer(lambda *a, **kw: results.append('DEFERRED NESTED'))
                        results.append('nested ends')
                except Failure:
                    pass
                defer(lambda *a, **kw: results.append('DEFERRED B'))
                results.append('ends')
        except Failure:
            pass
        self.failUnlessEqual(results, ['begins', 'nested begins', 'nested ends', 'ends', 'DEFERRED A', 'DEFERRED NESTED', 'DEFERRED B'], results)

    def test_commit_on_success_nested_failure(self):
        results = []
        try:
            with transaction.commit_on_success():
                results.append('begins')
                defer(lambda *a, **kw: results.append('DEFERRED A'))
                try:
                    with transaction.commit_on_success_unless_managed():
                        results.append('nested begins')
                        defer(lambda *a, **kw: results.append('DEFERRED NESTED'))
                        results.append('nested ends')
                        raise Failure
                except Failure:
                    pass
                defer(lambda *a, **kw: results.append('DEFERRED B'))
                results.append('ends')
        except Failure:
            pass
        # When using commit_on_success_unless_managed, DEFERRED NESTED is called even if the nested fails.
        self.failUnlessEqual(results, ['begins', 'nested begins', 'nested ends', 'ends', 'DEFERRED A', 'DEFERRED NESTED', 'DEFERRED B'], results)

    def test_commit_on_success_failure(self):
        results = []
        try:
            with transaction.commit_on_success():
                results.append('begins')
                defer(lambda *a, **kw: results.append('DEFERRED A'))
                try:
                    with transaction.commit_on_success_unless_managed():
                        results.append('nested begins')
                        defer(lambda *a, **kw: results.append('DEFERRED NESTED'))
                        results.append('nested ends')
                except Failure:
                    pass
                defer(lambda *a, **kw: results.append('DEFERRED B'))
                results.append('ends')
                raise Failure
        except Failure:
            pass
        self.failUnlessEqual(results, ['begins', 'nested begins', 'nested ends', 'ends'], results)

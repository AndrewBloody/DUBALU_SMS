# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

import warnings
from functools import wraps

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import memoize
from django.utils.encoding import force_bytes
from django.core import urlresolvers, signals

from dehydration import hydrate
from celery import signals as celery_signals


def get_swapped_model(swappable):
    """
    Returns the swappable Model that is active in this project.

    Swappable is in the form ``<APP_NAME>_<MODEL_NAME>_MODEL``.
    """
    from django.db.models import get_model

    try:
        app_label, model_name = getattr(settings, swappable).split('.')
    except ValueError:
        raise ImproperlyConfigured("%s must be of the form 'app_label.model_name'")
    model = get_model(app_label, model_name)
    if model is None:
        raise ImproperlyConfigured("%s refers to model '%s' that has not been installed" % (swappable, getattr(settings, swappable)))
    return model
get_swapped_model._cache = {}
get_swapped_model = memoize(get_swapped_model, get_swapped_model._cache, 1)


def on_task_prerun(sender, **kwargs):
    if not getattr(sender.run, '_django_task', False):
        return
    local_settings = kwargs['kwargs'].pop('local_settings', None)
    if not isinstance(local_settings, dict):
        warnings.warn("%s.%s task must be called with a valid local_settings named argument" % (sender.run.__module__, sender.run.__name__))
        return
    if not getattr(sender.request, 'is_eager', False):
        # Setup settings:
        try:
            from raven.contrib.django.models import client
        except ImportError:
            pass
        else:    
            # setting here
            client.set_dsn(settings.RAVEN_CONFIG['dsn'])
        sender.request.original_settings = settings.load()
        local_settings = hydrate(local_settings)
        settings.clear(local_settings)


def on_task_postrun(sender, **kwargs):
    if not getattr(sender.run, '_django_task', False):
        return
    if not getattr(sender.request, 'is_eager', False):
        original_settings = getattr(sender.request, 'original_settings', None)
        # Restore settings:
        try:
            from raven.contrib.django.models import client
        except ImportError:
            pass
        else:
            client.set_dsn(settings.RAVEN_CONFIG['dsn'])
        settings.clear(original_settings)
        


celery_signals.task_prerun.connect(on_task_prerun)
celery_signals.task_postrun.connect(on_task_postrun)


def django_task(func=None):
    """
    Decorator used mainly by celery tasks which sets up the settings, the urls
    and sends request signals as it was with the passed local settings.

    """
    def _django_task(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            # Modify get_urls with try
            from dfw.urls import get_urls

            signals.request_started.send(sender=func)

            urlpatterns = get_urls(settings.PROJECT_NAME, settings.PROJECT_SUFFIX)
            urlresolvers.set_urlconf(urlpatterns)
            ret = func(*args, **kwargs)

            signals.request_finished.send(sender=func)
            return ret
        wrapped._django_task = True
        return wrapped
    if callable(func):
        return _django_task(func)
    return _django_task


def cache_key_func(key, key_prefix, version):
    """
    KEY_FUNCTION = 'dfw.core.utils.cache_key_func'
    """
    return b':'.join((
        force_bytes(settings.STAGE),
        force_bytes(settings.PROJECT),
        force_bytes(settings.SITE_ID),
        force_bytes(key_prefix),
        force_bytes(version),
        force_bytes(key),
    ))

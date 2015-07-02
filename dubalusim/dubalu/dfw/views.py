# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

from django import http
from django.conf import settings
from django.template import Context, loader, TemplateDoesNotExist

from django.views.decorators.csrf import requires_csrf_token
from django.views.defaults import permission_denied as django_permission_denied, page_not_found as django_page_not_found


def _error(request, template_name, cls, message):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        return cls(message, content_type='text/html')
    if not hasattr(request, 'user'):
        request.user = None
    if not hasattr(request, 'entity'):
        request.entity = None
    if not hasattr(request, 'profile'):
        request.profile = None
    if not hasattr(request, 'site'):
        request.site = None
    return cls(template.render(Context({
        'BASE_TEMPLATE': settings.BASE_TEMPLATE if request.site else 'html.html',
        'request': request,
        'user': request.user,
    })))


@requires_csrf_token
def page_not_found(request, template_name='404.html'):
    """
    Default 404 handler.

    Templates: :template:`404.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
    """
    return django_page_not_found(request, template_name=template_name)


@requires_csrf_token
def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: :template:`500.html`
    Context: None
    """
    return _error(request, template_name, http.HttpResponseServerError, '<h1>Server Error (500)</h1>')


@requires_csrf_token
def bad_request(request, template_name='400.html'):
    """
    400 error handler.

    Templates: :template:`400.html`
    Context: None
    """
    return _error(request, template_name, http.HttpResponseBadRequest, '<h1>Bad Request (400)</h1>')


@requires_csrf_token
def permission_denied(request, template_name='403.html'):
    """
    Permission denied (403) handler.

    Templates: :template:`403.html`
    Context: None

    If the template does not exist, an Http403 response containing the text
    "403 Forbidden" (as per RFC 2616) will be returned.
    """
    return django_permission_denied(request, template_name=template_name)

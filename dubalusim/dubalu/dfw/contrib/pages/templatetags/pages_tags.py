# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

from django.contrib.sites import get_current_site
from django import template
register = template.Library()


@register.assignment_tag(takes_context=True)
def page(context):
    request = context['request']
    if not request.user.has_perm('can_edit_site', get_current_site(None)):
        return None
    return [0]


@register.simple_tag(takes_context=True)
def editable(context, element):
    request = context['request']
    if not element or not request.user.has_perm('can_edit_site', get_current_site(None)):
        return ''
    if isinstance(element, list):
        idx = element[0]
        element[0] += 1
    else:
        idx = element
    return '_ped_%s" contenteditable="true' % idx

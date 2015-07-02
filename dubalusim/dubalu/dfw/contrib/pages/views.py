# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

import os
import re

from lxml import html

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import DoesNotResolve  # This needs patch for [https://code.djangoproject.com/ticket/16774]
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.sites import get_current_site
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.files import locks

from dfw.utils import json

from dfw.core.storage import expand_path


EDITABLE_TAG_ID = '{% editable element %}'
EDITABLE_TAG_ID_E = EDITABLE_TAG_ID.replace('{', '\{').replace('}', '\}').replace('%', '\%').replace(' ', '\ ')

DJ_ESCAPED = (
    (('%7B%7B', '%7D%7D'), ('{{', '}}')),
    (('%7B%', '%%7D'), ('{%', '%}')),
    (('%7B#', '#%7D'), ('{#', '#}')),
)
DJ_ESCAPED_RE = re.compile('|'.join('(%s)(.*?)(%s)' % (re.escape(e[0][0]), re.escape(e[0][1])) for e in DJ_ESCAPED))
DJ_ESCAPED_Z = zip(*DJ_ESCAPED)
DJ_ESCAPED_TR = dict(zip((item for sublist in DJ_ESCAPED_Z[0] for item in sublist), (item for sublist in DJ_ESCAPED_Z[1] for item in sublist)))


def _django_fix(s):
    return DJ_ESCAPED_RE.sub(lambda m: ''.join((DJ_ESCAPED_TR.get(g, g) or '').replace('%20', ' ') for g in m.groups()), s)


def _guess_ind(pi):
    ind = ind1 = ind2 = ''

    pi1 = pi
    # if '        ' in pi1:
    #     ind1 = '        '
    #     pi1 = pi1.replace(ind1, '')
    if '    ' in pi1:
        ind1 = '    '
        pi1 = pi1.replace(ind1, '')
    if '  ' in pi1:
        ind1 = '  '
        pi1 = pi1.replace(ind1, '')
    ti1 = pi.count(ind1)
    ts1 = pi1.count(' ')

    pi2 = pi
    # if '      ' in pi2:
    #     ind2 = '      '
    #     pi2 = pi2.replace(ind2, '')
    if '   ' in pi2:
        ind2 = '   '
        pi2 = pi2.replace(ind2, '')
    ti2 = pi.count(ind2)
    ts2 = pi2.count(' ')

    if ts1 or ts2:
        if ts1 <= ts2 and ind1:
            ind = ind1
        else:
            ind = ind2
    elif ti1 or ti2:
        if ti1 >= ti2 and ind1:
            ind = ind1
        else:
            ind = ind2

    return ind


def _indent(elem, level=0, ind='\t', pi=None):
    if elem.text and '\n' in elem.text:
        nlevel = level + 1
        i = '\n' + level * ind
    else:
        nlevel = level
        i = ''
    if not elem.text or not elem.text.strip():
        elem.text = i
    if not elem.tail or not elem.tail.strip():
        elem.tail = pi
    for e in elem:
        _indent(e, nlevel, pi=i)
    if i and len(elem):
        if not e.tail or not e.tail.strip():
            e.tail = pi


@csrf_exempt
def page_fallback(request, *args, **kwargs):
    try:
        template_name = request.template_name
        extra_context = request.extra_context
    except AttributeError:
        raise DoesNotResolve
    else:
        return render(request, template_name, extra_context)


@require_http_methods(['POST'])
@login_required
def editor(request, path):
    """
    Receives a page chunk to be edited

    """
    # FIXME: Check permissions here!
    if not request.user.has_perm('can_edit_site', get_current_site(None)):
        raise PermissionDenied
    status = 'OK'
    message = ''
    path = path.strip('/') or 'index'
    base_path = expand_path(os.path.join("%s" % settings.NODE_ID, request.site.eid, 'pages'))
    path = os.path.join(settings.STORAGE_ROOT, base_path, path + '.html')
    try:
        data = request.POST['data']
        idx = request.POST['idx']
        idx = int(idx)  # Get the index from the element id
    except ValueError:
        try:
            # Create new element from user's data
            data = '<div>' + data + '</div>'  # Wrap data with the same tag as the wrapping element being edited
            data = html.tostring(html.fromstring(data), pretty_print=True).strip()[5:-6].strip()  # Pretty format whatever the user sent us

            idx = idx.upper()
            site = get_current_site(None)
            if idx.startswith('SITE_') and idx in site.get_context_data():
                site.context[idx] = data
                site.save()
            else:
                status = 'ERR'
                message = 'Invalid configuration!'

        except Exception as exc:
            status = 'ERR'
            message = "%s" % exc
            message = message.replace(os.path.join(settings.STORAGE_ROOT, base_path), '')
    else:
        try:
            page_html = open(path).read().decode('utf-8')  # Open the page
            e = html.fromstring('<div>' + page_html + '</div>')  # Get the whole page's html in a div (which later will be removed)
            el = e.cssselect('[id=%s]' % EDITABLE_TAG_ID_E)[idx]  # Locate element being edited

            # Create new element from user's data
            data = '<%s>' % el.tag + data + '</%s>' % el.tag  # Wrap data with the same tag as the wrapping element being edited
            data = html.tostring(html.fromstring(data), pretty_print=True)  # Pretty format whatever the user sent us
            nel = html.fromstring(data)  # Get the Element object

            # Figure out the current level and the indentation from the padding
            prev = el.getprevious()
            text = prev.tail if prev is not None else el.getparent().text
            _ = pi = text[:len(text) - len(text.lstrip())] if text else ''
            ind = _guess_ind(_)
            if '\t' in _ or not ind:
                if not ind:
                    ind = ' '
                if ind:
                    _ = _.expandtabs(len(ind)).replace(ind, '\t')
                ind = '\t'
            level = _.count(ind) + 1
            _indent(nel, level=level, ind=ind, pi=pi)  # Indent elements

            # Prepare new element
            nel.tail = el.tail
            for k, v in el.items():  # Fill attributes
                nel.set(k, v)

            el.getparent().replace(el, nel)  # Replace old with new element
            _html = html.tostring(e, encoding='utf-8').decode('utf-8').strip()[5:-6].strip() + '\n'  # Remove wrapping div
            _html = _django_fix(_html)  # Fix dango tags
            _html = _html.encode('utf-8')

            with open(path, 'w') as f:
                locks.lock(f, locks.LOCK_EX)
                f.write(_html)
        except Exception as exc:
            status = 'ERR'
            message = "%s" % exc
            message = message.replace(os.path.join(settings.STORAGE_ROOT, base_path), '')

    return HttpResponse(json.dumps({
        'status': status,
        'message': message
    }), content_type='application/json')

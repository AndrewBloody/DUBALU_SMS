# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns('dfw.contrib.pages.views',
    url(r'^editor(?P<path>/[-\w/]+/|/)$', 'editor', name='page_editor'),
    url(r'^.*/$', 'page_fallback'),
)

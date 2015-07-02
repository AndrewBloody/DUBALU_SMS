# -*- coding: utf-8 -*-

"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS
:copyright: Copyriht (c) 2013-2014, deipi.com LLC. All
:license: See LICENSE for license details

"""

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns('sample.smsapp.views', 
	url(r'^$', 'item_list', name='item-list'),
	url(r'^app/$', 'item_list', name='item-list2'),
	url(r'^add/$', 'item_create', name='item-add'),
	)
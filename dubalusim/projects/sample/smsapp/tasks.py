# -*- coding: utf-8 -*-
"""
Dubalu Framework: CFDI Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

import csv
from celery import task

from dfw.core.utils import django_task
from dehydration import hydrate

@task()
@django_task()
def test(txt):
	text = hydrate(txt)
	print '->',text



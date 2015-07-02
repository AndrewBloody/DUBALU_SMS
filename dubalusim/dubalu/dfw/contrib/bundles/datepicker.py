# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

from django_assets import Bundle

from . import Bundles


class Datepicker(Bundles):
    """
    Bootstrap Datepicker

    A datepicker for @twitter bootstrap forked from Stefan Petre's (of eyecon.ro), improvements by @eternicode

    [https://github.com/eternicode/bootstrap-datepicker]

    """
    js = Bundle(
        'src/js/bootstrap-datepicker.js',
        'src/js/bootstrap-datepicker/bootstrap-datepicker.es.js',
    )
    css = Bundle(
        'src/css/bootstrap-datepicker.scss',
    )

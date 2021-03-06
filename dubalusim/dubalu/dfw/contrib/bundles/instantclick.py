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


class InstantClick(Bundles):
    """
    InstantClick

    Library that makes navigation effectively instant in most cases.

    [http://instantclick.io/]

    """
    js = Bundle(
        'src/js/instantclick.js',
    )

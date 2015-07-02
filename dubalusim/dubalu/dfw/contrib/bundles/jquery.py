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


class jQuery(Bundles):
    """
    Basic JavaScript. Keep this as short as possible!

    """
    js = Bundle(
        'src/js/jquery.js',
        'src/js/asyncLoadScript.js',
    )


class jQueryExtra(Bundles):
    """
    jQuery essential plugins

    """
    js = Bundle(
        'src/js/jquery.easing.js',
        'src/js/jquery.cookie.js',
        'src/js/jquery.resize.js',
        'src/js/jquery.color.js',
        'src/js/jquery.livesetup.js',
        'src/js/jquery.closestDescendant.js',
        'src/js/jquery.sortElements.js',
    )

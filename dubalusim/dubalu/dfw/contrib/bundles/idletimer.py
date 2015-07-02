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


class IdleTimer(Bundles):
    """
    Fires a custom event when the user is "idle". Idle is defined by not...

    moving the mouse
    scrolling the mouse wheel
    using the keyboard.

    """
    js = Bundle(
        'src/js/jquery.idle-timer.js',
    )

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


class Tour(Bundles):
    """
    Bootstrap Tour

    Quick and easy product tours with Twitter Bootstrap Popovers

    """
    js = Bundle(
        'src/js/bootstrap-tour.js',
    )
    css = Bundle(
        'src/css/bootstrap-tour.scss',
    )

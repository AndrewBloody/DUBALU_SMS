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


class Ladda(Bundles):
    """
    Ladda UI for Bootstrap 3

    [downloaded from: https://github.com/msurguy/Ladda-bootstrap]
    """
    js = Bundle(
        'src/js/spin.js',
        'src/js/ladda.js',
        'src/js/jquery.ladda.js',
    )

    css = Bundle(
        'src/css/ladda.scss',
    )

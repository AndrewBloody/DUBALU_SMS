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


class Tokenfield(Bundles):
    """
    Tokenfield for Bootstrap

    [http://sliptree.github.io/bootstrap-tokenfield/]

    """
    js = Bundle(
        'src/js/bootstrap-tokenfield.js',
    )
    css = Bundle(
        'src/css/bootstrap-tokenfield/bootstrap-tokenfield.scss',
        'src/css/bootstrap-tokenfield/tokenfield-typeahead.scss',
    )

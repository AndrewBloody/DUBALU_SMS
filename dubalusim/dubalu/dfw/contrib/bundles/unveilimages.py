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


class UnveilImages(Bundles):
    """
    Unveil

    A very lightweight plugin to lazy load images for jQuery or Zepto.js

    [http://luis-almeida.github.io/unveil/]

    """
    css = Bundle(
        'src/css/jquery.unveil.scss',
    )
    js = Bundle(
        'src/js/jquery.unveil.js',
    )

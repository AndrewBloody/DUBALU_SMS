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


class Selectpicker(Bundles):
    """
    Bootstrap Select

    A custom select for @twitter bootstrap using button dropdown

    [https://github.com/silviomoreto/bootstrap-select]

    """
    js = Bundle(
        'src/js/bootstrap-select.js',
    )
    css = Bundle(
        'src/css/bootstrap-select.css',
    )

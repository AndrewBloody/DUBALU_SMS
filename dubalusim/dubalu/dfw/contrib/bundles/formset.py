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


class Formset(Bundles):
    """
    jQuery library to handle django formsets.

    """
    js = Bundle(
        'src/js/jquery.formsets.js',
    )

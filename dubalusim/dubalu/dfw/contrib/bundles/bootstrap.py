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


class Bootstrap(Bundles):
    """
    Bootstrap 3.1 CSS framework

    """
    css = Bundle(
        'src/css/bootstrap.scss',
        'src/css/bootstrap-overrides.scss',
    )


class BootstrapExtra(Bundles):
    """
    Bootstrap 3.1 w/ Jasny

    """
    js = Bundle(
        # Bootstrap
        ########################################
        'src/js/bootstrap/affix.js',
        'src/js/bootstrap/alert.js',
        'src/js/bootstrap/button.js',
        'src/js/bootstrap/carousel.js',
        'src/js/bootstrap/collapse.js',
        'src/js/bootstrap/dropdown.js',
        'src/js/bootstrap/tab.js',
        'src/js/bootstrap/transition.js',
        'src/js/bootstrap/scrollspy.js',
        'src/js/bootstrap/modal.js',
        'src/js/bootstrap/tooltip.js',
        'src/js/bootstrap/popover.js',

        # Jasny
        ########################################
        # 'src/js/jasny/fileinput.js',
        'src/js/jasny/inputmask.js',
        'src/js/jasny/offcanvas.js',
        'src/js/jasny/rowlink.js',
    )

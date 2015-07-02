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


class Ezpz(Bundles):
    """
    jQuery library to handle a file dropper.

    [downloaded from: http://www.jqueryscript.net/form/jQuery-Plugin-For-Drag-Drop-File-Input-Field-ezdz.html]
    """
    js = Bundle(
        'src/js/jquery.ezdz.js',
    )

    css = Bundle(
        'src/css/jquery.ezdz.scss',
    )

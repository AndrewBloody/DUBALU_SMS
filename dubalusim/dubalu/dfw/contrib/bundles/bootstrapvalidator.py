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


class BootstrapValidator(Bundles):
    """
    Bootstrap Validator

    A jQuery plugin to validate form fields. Use with Bootstrap 3

    [https://github.com/nghuuphuoc/bootstrapvalidator]

    """
    js = Bundle(
        'src/js/bootstrapValidator.js',
        'src/js/bootstrapValidator/between.js',
        'src/js/bootstrapValidator/callback.js',
        'src/js/bootstrapValidator/choice.js',
        'src/js/bootstrapValidator/creditCard.js',
        'src/js/bootstrapValidator/date.js',
        'src/js/bootstrapValidator/different.js',
        'src/js/bootstrapValidator/digits.js',
        'src/js/bootstrapValidator/emailAddress.js',
        'src/js/bootstrapValidator/greaterThan.js',
        'src/js/bootstrapValidator/hexColor.js',
        'src/js/bootstrapValidator/identical.js',
        'src/js/bootstrapValidator/lessThan.js',
        'src/js/bootstrapValidator/notEmpty.js',
        'src/js/bootstrapValidator/regexp.js',
        'src/js/bootstrapValidator/remote.js',
        'src/js/bootstrapValidator/stringLength.js',
        'src/js/bootstrapValidator/uri.js',
        'src/js/bootstrapValidator/zipCode.js',
    )
    css = Bundle(
        'src/css/bootstrapValidator.scss',
    )

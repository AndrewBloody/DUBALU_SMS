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


class AnimateCSS(Bundles):
    """
    animate.css: A cross-browser library of CSS animations. As easy to use as an easy thing.

    [downloaded from: https://github.com/daneden/animate.css]

    """
    attention_seekers = Bundle(
        'src/css/animate.css/attention_seekers/bounce.css',
        'src/css/animate.css/attention_seekers/flash.css',
        'src/css/animate.css/attention_seekers/pulse.css',
        'src/css/animate.css/attention_seekers/rubberBand.css',
        'src/css/animate.css/attention_seekers/shake.css',
        'src/css/animate.css/attention_seekers/swing.css',
        'src/css/animate.css/attention_seekers/tada.css',
        'src/css/animate.css/attention_seekers/wobble.css',
    )

    bouncing_entrances = Bundle(
        'src/css/animate.css/bouncing_entrances/bounceIn.css',
        'src/css/animate.css/bouncing_entrances/bounceInDown.css',
        'src/css/animate.css/bouncing_entrances/bounceInLeft.css',
        'src/css/animate.css/bouncing_entrances/bounceInRight.css',
        'src/css/animate.css/bouncing_entrances/bounceInUp.css',
    )

    bouncing_exits = Bundle(
        'src/css/animate.css/bouncing_exits/bounceOut.css',
        'src/css/animate.css/bouncing_exits/bounceOutDown.css',
        'src/css/animate.css/bouncing_exits/bounceOutLeft.css',
        'src/css/animate.css/bouncing_exits/bounceOutRight.css',
        'src/css/animate.css/bouncing_exits/bounceOutUp.css',
    )

    fading_entrances = Bundle(
        'src/css/animate.css/fading_entrances/fadeIn.css',
        'src/css/animate.css/fading_entrances/fadeInDown.css',
        'src/css/animate.css/fading_entrances/fadeInDownBig.css',
        'src/css/animate.css/fading_entrances/fadeInLeft.css',
        'src/css/animate.css/fading_entrances/fadeInLeftBig.css',
        'src/css/animate.css/fading_entrances/fadeInRight.css',
        'src/css/animate.css/fading_entrances/fadeInRightBig.css',
        'src/css/animate.css/fading_entrances/fadeInUp.css',
        'src/css/animate.css/fading_entrances/fadeInUpBig.css',
    )

    fading_exits = Bundle(
        'src/css/animate.css/fading_exits/fadeOut.css',
        'src/css/animate.css/fading_exits/fadeOutDown.css',
        'src/css/animate.css/fading_exits/fadeOutDownBig.css',
        'src/css/animate.css/fading_exits/fadeOutLeft.css',
        'src/css/animate.css/fading_exits/fadeOutLeftBig.css',
        'src/css/animate.css/fading_exits/fadeOutRight.css',
        'src/css/animate.css/fading_exits/fadeOutRightBig.css',
        'src/css/animate.css/fading_exits/fadeOutUp.css',
        'src/css/animate.css/fading_exits/fadeOutUpBig.css',
    )

    flippers = Bundle(
        'src/css/animate.css/flippers/flip.css',
        'src/css/animate.css/flippers/flipInX.css',
        'src/css/animate.css/flippers/flipInY.css',
        'src/css/animate.css/flippers/flipOutX.css',
        'src/css/animate.css/flippers/flipOutY.css',
    )

    lightspeed = Bundle(
        'src/css/animate.css/lightspeed/lightSpeedIn.css',
        'src/css/animate.css/lightspeed/lightSpeedOut.css',
    )

    rotating_entrances = Bundle(
        'src/css/animate.css/rotating_entrances/rotateIn.css',
        'src/css/animate.css/rotating_entrances/rotateInDownLeft.css',
        'src/css/animate.css/rotating_entrances/rotateInDownRight.css',
        'src/css/animate.css/rotating_entrances/rotateInUpLeft.css',
        'src/css/animate.css/rotating_entrances/rotateInUpRight.css',
    )

    rotating_exits = Bundle(
        'src/css/animate.css/rotating_exits/rotateOut.css',
        'src/css/animate.css/rotating_exits/rotateOutDownLeft.css',
        'src/css/animate.css/rotating_exits/rotateOutDownRight.css',
        'src/css/animate.css/rotating_exits/rotateOutUpLeft.css',
        'src/css/animate.css/rotating_exits/rotateOutUpRight.css',
    )

    sliders = Bundle(
        'src/css/animate.css/sliders/slideInDown.css',
        'src/css/animate.css/sliders/slideInLeft.css',
        'src/css/animate.css/sliders/slideInRight.css',
        'src/css/animate.css/sliders/slideInUp.css',
        'src/css/animate.css/sliders/slideOutDown.css',
        'src/css/animate.css/sliders/slideOutLeft.css',
        'src/css/animate.css/sliders/slideOutRight.css',
        'src/css/animate.css/sliders/slideOutUp.css',
    )

    specials = Bundle(
        'src/css/animate.css/specials/hinge.css',
        'src/css/animate.css/specials/rollIn.css',
        'src/css/animate.css/specials/rollOut.css',
    )

    css = Bundle(
        'src/css/animate.css/_base.css',
        attention_seekers,
        bouncing_entrances,
        bouncing_exits,
        fading_entrances,
        fading_exits,
        flippers,
        lightspeed,
        rotating_entrances,
        rotating_exits,
        sliders,
        specials,
    )

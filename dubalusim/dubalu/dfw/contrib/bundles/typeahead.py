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


class Typeahead(Bundles):
    """
    Twitter's Typeahead.js

    """
    js = Bundle(
        'src/js/typeahead.js/common/utils.js',
        'src/js/typeahead.js/bloodhound/version.js',
        'src/js/typeahead.js/bloodhound/tokenizers.js',
        'src/js/typeahead.js/bloodhound/lru_cache.js',
        'src/js/typeahead.js/bloodhound/persistent_storage.js',
        'src/js/typeahead.js/bloodhound/transport.js',
        'src/js/typeahead.js/bloodhound/search_index.js',
        'src/js/typeahead.js/bloodhound/options_parser.js',
        'src/js/typeahead.js/bloodhound/bloodhound.js',
        'src/js/typeahead.js/typeahead/html.js',
        'src/js/typeahead.js/typeahead/css.js',
        'src/js/typeahead.js/typeahead/event_bus.js',
        'src/js/typeahead.js/typeahead/event_emitter.js',
        'src/js/typeahead.js/typeahead/highlight.js',
        'src/js/typeahead.js/typeahead/input.js',
        'src/js/typeahead.js/typeahead/dataset.js',
        'src/js/typeahead.js/typeahead/dropdown.js',
        'src/js/typeahead.js/typeahead/typeahead.js',
        'src/js/typeahead.js/typeahead/plugin.js',
    )
    css = Bundle(
        'src/css/typeahead.scss',
    )

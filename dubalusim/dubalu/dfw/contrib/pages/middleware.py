# -*- coding: utf-8 -*-
"""
Dubalu Framework
~~~~~~~~~~~~~~~~

:author: Dubalu Framework Team. See AUTHORS.
:copyright: Copyright (c) 2013-2014, deipi.com LLC. All Rights Reserved.
:license: See LICENSE for license details.

"""
from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings
from django.template.loader import get_template, TemplateDoesNotExist

from dfw.core.storage import expand_path


class PagesMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'site'), "The Pages middleware requires sites middleware to be installed before it. Edit your MIDDLEWARE_CLASSES setting to insert 'dfw.profiles.sites.middleware.CurrentSiteMiddleware'."
        path = request.path
        path = path.strip('/') or 'index'
        base_path = expand_path(os.path.join("%s" % settings.NODE_ID, request.site.eid, 'pages'))

        template_name = os.path.join(settings.PROJECT_SUFFIX, base_path, path + '.html')
        try:
            get_template(template_name)
        except TemplateDoesNotExist:
            # import traceback; traceback.print_exc();
            pass
        else:
            request.template_name = template_name
            request.extra_context = {}

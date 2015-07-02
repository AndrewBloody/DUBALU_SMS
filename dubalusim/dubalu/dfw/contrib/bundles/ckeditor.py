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


class CKEditor(Bundles):
    """
    CKEditor 4

    """
    js = Bundle(
        ########################################################################
        # Core (js/CKEditor/core)
        'src/CKEditor/core/ckeditor_base.js',  # -
        'src/CKEditor/core/event.js',  # -
        'src/CKEditor/core/editor_basic.js',  # event
        'src/CKEditor/core/env.js',  # -
        'src/CKEditor/core/ckeditor_basic.js',  # editor_basic, env, event
        'src/CKEditor/core/dom.js',  # -
        'src/CKEditor/core/tools.js',  # env
        'src/CKEditor/core/dtd.js',  # tools
        'src/CKEditor/core/dom/event.js',  # -
        'src/CKEditor/core/dom/domobject.js',  # dom/event
        'src/CKEditor/core/dom/node.js',  # dom/domobject, tools
        'src/CKEditor/core/dom/window.js',  # dom/domobject
        'src/CKEditor/core/dom/document.js',  # dom/node, dom/window
        'src/CKEditor/core/dom/nodelist.js',  # dom/node
        'src/CKEditor/core/dom/element.js',  # dom, dom/document, dom/domobject, dom/node, dom/nodelist, tools
        'src/CKEditor/core/dom/walker.js',  # dom/node
        'src/CKEditor/core/dom/documentfragment.js',  # dom/element
        'src/CKEditor/core/dom/range.js',  # dom/document, dom/documentfragment, dom/element, dom/walker
        'src/CKEditor/core/dom/iterator.js',  # dom/range
        'src/CKEditor/core/htmlparser.js',  # -
        'src/CKEditor/core/htmlparser/basicwriter.js',  # htmlparser
        'src/CKEditor/core/htmlparser/node.js',  # htmlparser
        'src/CKEditor/core/htmlparser/comment.js',  # htmlparser, htmlparser/node
        'src/CKEditor/core/htmlparser/text.js',  # htmlparser, htmlparser/node
        'src/CKEditor/core/htmlparser/cdata.js',  # htmlparser, htmlparser/node
        'src/CKEditor/core/htmlparser/fragment.js',  # htmlparser, htmlparser/comment, htmlparser/text, htmlparser/cdata
        'src/CKEditor/core/htmlparser/filter.js',  # htmlparser
        'src/CKEditor/core/htmlparser/element.js',  # htmlparser, htmlparser/fragment, htmlparser/node
        'src/CKEditor/core/command.js',  # -
        'src/CKEditor/core/keystrokehandler.js',  # event
        'src/CKEditor/core/lang.js',  # -
        'src/CKEditor/lang/en.js',  # !lang
        # 'src/CKEditor/lang/es.js',  # !lang
        'src/CKEditor/core/scriptloader.js',  # dom/element, env
        'src/CKEditor/core/resourcemanager.js',  # scriptloader, tools
        'src/CKEditor/core/plugins.js',  # resourcemanager
        'src/CKEditor/core/ui.js',  # -
        'src/CKEditor/core/filter.js',  # dtd, tools
        'src/CKEditor/core/focusmanager.js',  # -
        'src/CKEditor/core/config.js',  # ckeditor_base
        'src/CKEditor/config.js',
        'src/CKEditor/core/editor.js',  # command, config, editor_basic, filter, focusmanager, keystrokehandler, lang, plugins, tools, ui
        'src/CKEditor/core/template.js',  # -
        'src/CKEditor/core/htmldataprocessor.js',  # htmlparser, htmlparser/basicwriter, htmlparser/fragment, htmlparser/filter
        'src/CKEditor/core/ckeditor.js',  # ckeditor_basic, dom, dtd, dom/document, dom/element, dom/iterator, editor, event, htmldataprocessor, htmlparser, htmlparser/element, htmlparser/fragment, htmlparser/filter, htmlparser/basicwriter, template, tools
        'src/CKEditor/core/editable.js',  # editor, tools, !ckeditor
        'src/CKEditor/core/selection.js',  # dom/range, dom/walker
        'src/CKEditor/core/style.js',  # selection
        'src/CKEditor/styles.js',  # !style
        'src/CKEditor/core/creators/inline.js',  # !editor
        'src/CKEditor/core/creators/themedui.js',  # !editor
        'src/CKEditor/core/dom/comment.js',  # dom/node
        'src/CKEditor/core/dom/elementpath.js',  # dom/element
        'src/CKEditor/core/dom/text.js',  # m/node, dom/domobject
        'src/CKEditor/core/dom/rangelist.js',  # dom/range
        'src/CKEditor/core/skin.js',  # -
        'src/CKEditor/skins/bootstrapck/skin.js',  # !skin
        'src/CKEditor/core/_bootstrap.js',  # config, creators/inline, creators/themedui, editable, ckeditor, plugins, scriptloader, style, tools, dom/comment, dom/elementpath, dom/text, dom/rangelist, skin
        ########################################################################
        # Plugins (js/CKEditor/plugins)
        'src/CKEditor/plugins/dialogui/plugin.js',  # -
        'src/CKEditor/plugins/dialog/plugin.js',  # dialogui
        'src/CKEditor/plugins/fakeobjects/plugin.js',  # -
        'src/CKEditor/plugins/fakeobjects/lang/en.js',
        # 'src/CKEditor/plugins/fakeobjects/lang/es.js',
        'src/CKEditor/plugins/indent/plugin.js',  # -
        'src/CKEditor/plugins/indent/lang/en.js',
        # 'src/CKEditor/plugins/indent/lang/es.js',
        'src/CKEditor/plugins/button/plugin.js',  # -
        'src/CKEditor/plugins/button/lang/en.js',
        # 'src/CKEditor/plugins/button/lang/es.js',
        'src/CKEditor/plugins/panel/plugin.js',  # -
        'src/CKEditor/plugins/floatpanel/plugin.js',  # panel
        'src/CKEditor/plugins/listblock/plugin.js',  # panel
        'src/CKEditor/plugins/richcombo/plugin.js',  # floatpanel, listblock, button
        ###
        # 'src/CKEditor/plugins/about/plugin.js',  # dialog
        # 'src/CKEditor/plugins/about/lang/en.js',
        # 'src/CKEditor/plugins/about/dialogs/about.js',  # dialog
        'src/CKEditor/plugins/basicstyles/plugin.js',  # -
        'src/CKEditor/plugins/basicstyles/lang/en.js',
        'src/CKEditor/plugins/clipboard/plugin.js',  # dialog
        'src/CKEditor/plugins/clipboard/lang/en.js',
        'src/CKEditor/plugins/clipboard/dialogs/paste.js',  # dialog
        'src/CKEditor/plugins/enterkey/plugin.js',  # -
        'src/CKEditor/plugins/entities/plugin.js',  # -
        'src/CKEditor/plugins/floatingspace/plugin.js',  # -
        'src/CKEditor/plugins/indentlist/plugin.js',  # indent
        'src/CKEditor/plugins/link/plugin.js',  # dialog, fakeobjects
        'src/CKEditor/plugins/link/lang/en.js',
        'src/CKEditor/plugins/link/dialogs/link.js',  # dialog
        'src/CKEditor/plugins/link/dialogs/anchor.js',  # dialog
        'src/CKEditor/plugins/list/plugin.js',  # indentlist
        'src/CKEditor/plugins/list/lang/en.js',
        'src/CKEditor/plugins/toolbar/plugin.js',  # button
        'src/CKEditor/plugins/toolbar/lang/en.js',
        'src/CKEditor/plugins/undo/plugin.js',  # -
        'src/CKEditor/plugins/undo/lang/en.js',
        # 'src/CKEditor/plugins/wysiwygarea/plugin.js',  # -
        'src/CKEditor/plugins/justify/plugin.js',  # -
        'src/CKEditor/plugins/justify/lang/en.js',
        'src/CKEditor/plugins/blockquote/plugin.js',  # -
        'src/CKEditor/plugins/blockquote/lang/en.js',
        'src/CKEditor/plugins/format/plugin.js',  # richcombo
        'src/CKEditor/plugins/format/lang/en.js',
        ########################################################################
        'src/CKEditor/setup.js',
    )
    css = Bundle(
        'src/CKEditor/skins/bootstrapck/scss/components/editor.scss',
        'src/CKEditor/skins/bootstrapck/scss/dialog/dialog.scss',
        'src/CKEditor/overrides.scss',
    )
    css_gecko = Bundle(
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/gecko/editor_gecko.scss',
        'src/CKEditor/skins/bootstrapck/scss/dialog/dialog.scss',
        'src/CKEditor/overrides.scss',
    )
    css_ie = Bundle(
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/ie/editor_ie.scss',
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/ie/dialog_ie.scss',
        'src/CKEditor/overrides.scss',
    )
    css_ie7 = Bundle(
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/ie7/editor_ie7.scss',
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/ie7/dialog_ie7.scss',
        'src/CKEditor/overrides.scss',
    )
    css_ie8 = Bundle(
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/ie8/editor_ie8.scss',
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/ie8/dialog_ie8.scss',
        'src/CKEditor/overrides.scss',
    )
    css_iequirks = Bundle(
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/iequirks/editor_iequirks.scss',
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/iequirks/dialog_iequirks.scss',
        'src/CKEditor/overrides.scss',
    )
    css_opera = Bundle(
        'src/CKEditor/skins/bootstrapck/scss/components/editor.scss',
        'src/CKEditor/skins/bootstrapck/scss/browser-specific/opera/dialog_opera.scss',
        'src/CKEditor/overrides.scss',
    )

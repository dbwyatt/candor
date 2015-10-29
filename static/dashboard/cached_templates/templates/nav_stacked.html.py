# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1443761713.919366
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\dashboard\\templates/nav_stacked.html'
_template_uri = 'nav_stacked.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<nav class="navbar-stacked">\r\n\t<ul>\r\n\t\t<li class="toolbar-button" data-target="/sell/post/"><i class="fa fa-plus fa-fw" style="position:relative;top:3px;"></i></li>\r\n\t\t<li class="toolbar-button" data-target="/sell/edit/"><i class="fa fa-pencil-square-o fa-fw" style="position:relative;top:3px;left:2px;"></i></li>\r\n\t\t<span class="spacer"></span>\r\n\t\t<li class="toolbar-button" data-target="/dashboard/"><i class="fa fa-dashboard fa-fw"></i></li>\r\n\t\t<li class="toolbar-button" data-target="messages/"><i class="fa fa-envelope fa-fw"><span class="badge badge-red">3</span></i></li>\r\n\t\t<li class="toolbar-button help" data-target="help/"><i class="fa fa-question-circle fa-fw" style="position:relative;"></i></li>\r\n\t</ul>\r\n</nav>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "nav_stacked.html", "line_map": {"16": 0, "27": 21, "21": 1}, "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\dashboard\\templates/nav_stacked.html"}
__M_END_METADATA
"""

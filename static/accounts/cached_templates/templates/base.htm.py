# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446091801.844197
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\accounts\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['rightlinks', 'content']


from django_mako_plus.controller import static_files 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def rightlinks():
            return render_rightlinks(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n')
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n<head>\r\n\r\n    <title>Account</title>\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n</head>\r\n<body>\r\n\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'rightlinks'):
            context['self'].rightlinks(**pageargs)
        

        __M_writer('\r\n  \r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \r\n  \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  \r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_rightlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def rightlinks():
            return render_rightlinks(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <li><a href="/homepage/">Home</a></li>\r\n        <li><a href="/homepage/#about">About</a></li>\r\n        <li><a href="/homepage/#contact">Contact</a></li>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n        Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "source_encoding": "utf-8", "line_map": {"64": 118, "65": 118, "66": 118, "72": 107, "78": 107, "16": 4, "84": 113, "90": 113, "29": 0, "96": 90, "40": 2, "41": 4, "42": 5, "46": 5, "47": 6, "48": 16, "49": 19, "50": 19, "51": 19, "52": 46, "53": 106, "58": 111, "63": 115}, "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\accounts\\templates/base.htm"}
__M_END_METADATA
"""

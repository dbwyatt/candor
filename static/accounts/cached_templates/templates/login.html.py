# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1437184123.01921
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\accounts\\templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


import datetime 

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
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="login-container">\r\n\t\t<span class="login-text">Login with your Google or Facebook account</span>\r\n\t\t<div class="btn-wrapper">\t\r\n\t\t\t<div id="my-signin2" class="btn btn-block btn-social btn-google" data-onsuccess="onSignIn">\r\n\t\t\t\t<i class="fa fa-google"></i> Sign in with Google\r\n\t\t\t</div>\r\n\r\n\t\t\t<span class="spacer"></span>\r\n\r\n\t\t\t<a class="btn btn-block btn-social btn-facebook" data-onsuccess="onSignIn">\r\n\t\t\t\t<i class="fa fa-facebook"></i> Sign in with Facebook\r\n\t\t\t</a>\r\n\t\t</div>\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\accounts\\templates/login.html", "source_encoding": "utf-8", "line_map": {"16": 2, "53": 4, "36": 1, "37": 2, "59": 53, "29": 0, "47": 4}, "uri": "login.html"}
__M_END_METADATA
"""

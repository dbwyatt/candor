# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446091801.822198
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\accounts\\templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="content">\r\n\t    <address>\r\n\t\t\t<img class="user-img" src="')
        __M_writer(str( request.session['user']['image'] ))
        __M_writer('" /><br><br>\r\n\t\t\t<strong><span class="name">')
        __M_writer(str( request.session['user']['name'][0] ))
        __M_writer(' ')
        __M_writer(str( request.session['user']['name'][1] ))
        __M_writer('</span></strong><br>\r\n\t\t</address>\r\n\t\t<address>\r\n\t\t\t<strong>Username</strong><br>\r\n\t\t\t<span class="username">')
        __M_writer(str( request.session['user']['email'] ))
        __M_writer('</span><br>\r\n\t\t\t<br>\r\n\t\t\t<strong>Email</strong><br>\r\n\t\t\t<span class="email">')
        __M_writer(str( request.session['user']['email'] ))
        __M_writer('</span><br>\r\n')
        __M_writer('\t\t\t<br>\r\n\t\t\t<strong>Last Login</strong><br>\r\n\t\t\t<span class="creation-date">\r\n')
        __M_writer('\t\t\t\t')
        __M_writer(str( request.session['user']['last_login']['date'] ))
        __M_writer(' ')
        __M_writer(str( request.session['user']['last_login']['time'] ))
        __M_writer('\r\n\t\t\t</span>\r\n\t\t</address>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "source_encoding": "utf-8", "line_map": {"64": 15, "65": 15, "66": 26, "67": 30, "68": 30, "69": 30, "70": 30, "71": 30, "77": 71, "16": 2, "29": 0, "37": 1, "38": 2, "48": 4, "55": 4, "56": 7, "57": 7, "58": 8, "59": 8, "60": 8, "61": 8, "62": 12, "63": 12}, "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\accounts\\templates/index.html"}
__M_END_METADATA
"""

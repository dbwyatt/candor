# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446092066.660874
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor/dashboard/templates/index.html'
_template_uri = '/dashboard/templates/index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['footer', 'title', 'content']


from datetime import datetime 

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
        messages = context.get('messages', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div></div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<title>Candor Contracts</title>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="main-container">\r\n\r\n\t\t')
        runtime._include_file(context, '/dashboard/templates/nav_stacked.html', _template_uri)
        __M_writer('\r\n\r\n\t\t<div id="action-container">\r\n\t\t\t<span style="font-size: 51px; font-family: Tahoma, Geneva, sans-serif;">Welcome</span>\r\n            <br>\r\n            <div class="panel panel-default recent-search">\r\n\r\n            </div>\r\n\r\n            <div class="panel panel-default message">\r\n                <div class="panel-heading"><h3 class="panel-title">Recent Messages</h3></div>\r\n')
        for message in messages:
            __M_writer('                    <div class="message-container">\r\n                        <div class="message-text">')
            __M_writer(str( message.message ))
            __M_writer('</div>\r\n                        <div class="message-date">')
            __M_writer(str( datetime.strftime(message.time_sent, '%A, %B %d, %Y') ))
            __M_writer('<br>')
            __M_writer(str( datetime.strftime(message.time_sent, '%I:%M %p').lstrip("0") ))
            __M_writer('</div>\r\n                        <div class="message-from">')
            __M_writer(str( message.from_user.name ))
            __M_writer('</div>\r\n                    </div>\r\n')
        __M_writer('            </div>\r\n            <div class="panel panel-default post"></div>\r\n            <div class="panel panel-default"></div>\r\n        </div>\r\n\r\n\r\n\t\t<footer>\r\n            Copyright &copy; ')
        __M_writer(str( datetime.now().year ))
        __M_writer(' Candor Contracts\r\n        </footer>\r\n\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/dashboard/templates/index.html", "source_encoding": "utf-8", "line_map": {"68": 42, "74": 4, "80": 4, "86": 8, "47": 6, "93": 8, "94": 11, "95": 11, "96": 22, "97": 23, "98": 24, "99": 24, "100": 25, "101": 25, "102": 25, "103": 25, "104": 26, "41": 1, "42": 2, "107": 36, "108": 36, "29": 0, "114": 108, "52": 40, "105": 26, "106": 29, "62": 42, "16": 2}, "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor/dashboard/templates/index.html"}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434866434.473982
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\homepage\\templates/contact_email.html'
_template_uri = 'contact_email.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        sender = context.get('sender', UNDEFINED)
        sender_email = context.get('sender_email', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sender = context.get('sender', UNDEFINED)
        sender_email = context.get('sender_email', UNDEFINED)
        def content():
            return render_content(context)
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<b>From</b>: ')
        __M_writer(str( sender ))
        __M_writer('\r\n\t<br>\r\n\t<b>Email</b>: ')
        __M_writer(str( sender_email ))
        __M_writer('\r\n\t<br><br>\r\n\t')
        __M_writer(str( message ))
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "contact_email.html", "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\homepage\\templates/contact_email.html", "line_map": {"59": 6, "68": 62, "37": 1, "56": 3, "57": 4, "58": 4, "27": 0, "60": 6, "61": 8, "62": 8, "47": 3}}
__M_END_METADATA
"""

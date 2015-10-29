# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434867292.4948943
_enable_loop = True
_template_filename = '/var/www/dev/Candor/homepage/templates/contact_email.html'
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
        message = context.get('message', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        sender = context.get('sender', UNDEFINED)
        sender_email = context.get('sender_email', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        message = context.get('message', UNDEFINED)
        def content():
            return render_content(context)
        sender = context.get('sender', UNDEFINED)
        sender_email = context.get('sender_email', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t<b>From</b>: ')
        __M_writer(str( sender ))
        __M_writer('\n\t<br>\n\t<b>Email</b>: ')
        __M_writer(str( sender_email ))
        __M_writer('\n\t<br><br>\n\t')
        __M_writer(str( message ))
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact_email.html", "source_encoding": "utf-8", "line_map": {"59": 6, "68": 62, "37": 1, "56": 3, "57": 4, "58": 4, "27": 0, "60": 6, "61": 8, "62": 8, "47": 3}, "filename": "/var/www/dev/Candor/homepage/templates/contact_email.html"}
__M_END_METADATA
"""

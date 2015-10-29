# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434867304.411582
_enable_loop = True
_template_filename = '/var/www/dev/Candor/homepage/templates/contact_form.html'
_template_uri = 'contact_form.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        csrf_token = context.get('csrf_token', UNDEFINED)
        contact = context.get('contact', UNDEFINED)
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
        def content():
            return render_content(context)
        csrf_token = context.get('csrf_token', UNDEFINED)
        contact = context.get('contact', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t<form id="contact-form" method="POST" action="/homepage/index.contact/">\n\t\t<label>Send us a message here</label>\n\t\t')
        __M_writer(str( contact ))
        __M_writer('\n')
        __M_writer('\t\t<input type="submit" class="btn btn-primary" value="Send" />\n\t\t<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(str( csrf_token ))
        __M_writer("' />\n\t</form>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact_form.html", "source_encoding": "utf-8", "line_map": {"65": 59, "59": 9, "36": 1, "54": 3, "55": 6, "56": 6, "57": 8, "58": 9, "27": 0, "46": 3}, "filename": "/var/www/dev/Candor/homepage/templates/contact_form.html"}
__M_END_METADATA
"""

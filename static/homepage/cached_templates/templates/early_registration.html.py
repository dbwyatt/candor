# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434602541.067941
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\homepage\\templates/early_registration.html'
_template_uri = 'early_registration.html'
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
        csrf_token = context.get('csrf_token', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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
        csrf_token = context.get('csrf_token', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<form id="sign-up" method="POST" action="/homepage/index.register/">\t\r\n\t\t<label>Sign up for early registration</label>\r\n\t\t')
        __M_writer(str( form ))
        __M_writer('\r\n\t\t<sup>*Your email will not be used for anything other than to contact you when Candor is ready to be tested</sup>\r\n\t\t<input type="submit" class="btn btn-primary" value="Sign Up" />\r\n\t\t<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(str( csrf_token ))
        __M_writer("' />\r\n\t</form>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 58, "36": 1, "54": 3, "55": 6, "56": 6, "57": 9, "58": 9, "27": 0, "46": 3}, "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\homepage\\templates/early_registration.html", "source_encoding": "utf-8", "uri": "early_registration.html"}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1443843544.235089
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\sell\\templates/edit.html'
_template_uri = 'edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['footer', 'content', 'navigation']


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
    return runtime._inherit_from(context, '/dashboard/templates/index.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def navigation():
            return render_navigation(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        environment = context.get('environment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation'):
            context['self'].navigation(**pageargs)
        

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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="main-container">\r\n    \r\n\t\t')
        runtime._include_file(context, '/dashboard/templates/nav_stacked.html', _template_uri)
        __M_writer('\r\n\r\n\t\t<div id="action-container">\r\n\t\t\tedit\r\n\t\t</div>\r\n\r\n\t\t<footer>\r\n            Copyright &copy; ')
        __M_writer(str( datetime.now().year ))
        __M_writer(' Candor Contracts\r\n        </footer>\r\n\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def navigation():
            return render_navigation(context)
        environment = context.get('environment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('        <nav class="navbar navbar-default navbar-fixed-top">\r\n            <div class="container">\r\n                <!-- Brand and toggle get grouped for better mobile display -->\r\n                <div class="navbar-header">\r\n                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n                        <span class="sr-only">Toggle navigation</span>\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span>\r\n                    </button>\r\n                    <a class="navbar-brand" href="/"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/candor.png" />\r\n                        <span class="brand-text">\r\n')
        if environment != '/var/www/candor':
            __M_writer('                                Candor Contracts Dev\r\n')
        else:
            __M_writer('                                Candor Contracts\r\n')
        __M_writer('                        </span>\r\n                    </a>\r\n                </div>\r\n\r\n                <!-- Collect the nav links, forms, and other content for toggling -->\r\n                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                    <ul class="nav navbar-nav">\r\n                        <!-- <li><a href="#">Link <span class="sr-only">(current)</span></a></li>\r\n                        <li><a href="#">Link</a></li>\r\n                        <li class="dropdown">\r\n                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\r\n                            <ul class="dropdown-menu" role="menu">\r\n                                <li><a href="#">Action</a></li>\r\n                                <li><a href="#">Another action</a></li>\r\n                                <li><a href="#">Something else here</a></li>\r\n                                <li class="divider"></li>\r\n                                <li><a href="#">Separated link</a></li>\r\n                                <li class="divider"></li>\r\n                                <li><a href="#">One more separated link</a></li>\r\n                            </ul>\r\n                        </li> -->\r\n')
        __M_writer('                    </ul>\r\n                    <ul class="nav navbar-nav navbar-right">\r\n                        <!-- <li><a href="#">Link</a></li>\r\n                        <li class="dropdown">\r\n                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\r\n                            <ul class="dropdown-menu" role="menu">\r\n                                <li><a href="#">Action</a></li>\r\n                                <li><a href="#">Another action</a></li>\r\n                                <li><a href="#">Something else here</a></li>\r\n                                <li class="divider"></li>\r\n                                <li><a href="#">Separated link</a></li>\r\n                            </ul>\r\n                        </li> -->\r\n')
        __M_writer('                            <li><a href="/">Home</a></li>\r\n                            <li><a href="/homepage/#about">About</a></li>\r\n                            <li><a href="/homepage/#contact">Contact</a></li>\r\n')
        if 'user' not in request.session:
            __M_writer('                            <li><a href="#" class="sign-in">Sign In</a></li>\r\n')
        else:
            __M_writer('                            <li class="dropdown">\r\n                                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="name">Hello, ')
            __M_writer(str( request.session['user']['name'][0] ))
            __M_writer('</span><span class="account">Your Account</span> <span class="caret"></span></a>\r\n                                <ul class="dropdown-menu" role="menu">\r\n                                    <li><a href="/accounts/">Account</a></li>\r\n                                    <li><a href="#">Another action</a></li>\r\n                                    <li><a href="#">Something else here</a></li>\r\n                                    <li class="divider"></li>\r\n                                    <li><a href="#" onclick=signOut()>Logout</a></li>\r\n                                </ul>\r\n                            </li>\r\n')
        __M_writer('                    </ul>\r\n                </div><!-- /.navbar-collapse -->\r\n            </div><!-- /.container-fluid -->\r\n        </nav>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\sell\\templates/edit.html", "line_map": {"64": 105, "107": 20, "118": 82, "70": 105, "113": 68, "108": 21, "76": 89, "16": 2, "82": 89, "83": 92, "84": 92, "85": 99, "86": 99, "92": 4, "29": 0, "101": 4, "102": 6, "103": 16, "104": 16, "105": 18, "106": 19, "43": 1, "44": 2, "109": 23, "110": 49, "111": 63, "112": 67, "49": 87, "114": 69, "115": 70, "116": 71, "117": 71, "54": 103, "124": 118}, "uri": "edit.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1439049217.705252
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\sell\\templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        environment = context.get('environment', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def navigation():
            return render_navigation(context._locals(__M_locals))
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
        __M_writer('\r\n\t<div id="main-container">\r\n\t\t<nav class="navbar-stacked">\r\n\t\t\t<ul>\r\n\t\t\t\t<li class="toolbar-button" data-target="post"><i class="fa fa-plus fa-fw" style="position:relative;top:3px;"></i></li>\r\n\t\t\t\t<li class="toolbar-button" data-target="edit"><i class="fa fa-pencil-square-o fa-fw" style="position:relative;top:3px;left:2px;"></i></li>\r\n\t\t\t\t<span class="spacer"></span>\r\n\t\t\t\t<li class="toolbar-button" data-target="dashboard"><i class="fa fa-dashboard fa-fw"></i></li>\r\n\t\t\t\t<li class="toolbar-button" data-target="messages"><i class="fa fa-envelope fa-fw"><span class="badge badge-red">3</span></i></li>\r\n\t\t\t\t<li class="toolbar-button help" data-target="help"><i class="fa fa-question-circle fa-fw" style="position:relative;top:3px;"></i></li>\r\n\t\t\t</ul>\r\n\t\t</nav>\r\n\r\n\t\t<div id="action-container">\r\n\t\t\t<span style="font-size: 51px; font-family: Tahoma, Geneva, sans-serif;">Welcome</span><br><span style="font-size: 25px;">to your</span><br><span style="font-size: 39px;">dashboard</span>\r\n\t\t</div>\r\n\r\n\t\t<footer>\r\n            Copyright &copy; ')
        __M_writer(str( datetime.now().year ))
        __M_writer(' Candor Contracts\r\n        </footer>\r\n\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        environment = context.get('environment', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def navigation():
            return render_navigation(context)
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
{"line_map": {"64": 113, "107": 23, "70": 113, "113": 70, "108": 49, "76": 89, "16": 2, "82": 89, "83": 107, "84": 107, "90": 4, "29": 0, "99": 4, "100": 6, "101": 16, "102": 16, "103": 18, "104": 19, "105": 20, "106": 21, "43": 1, "44": 2, "109": 63, "110": 67, "111": 68, "112": 69, "49": 87, "114": 71, "115": 71, "116": 82, "54": 111, "122": 116}, "source_encoding": "utf-8", "uri": "index.html", "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\sell\\templates/index.html"}
__M_END_METADATA
"""

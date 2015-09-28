# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434842052.7788315
_enable_loop = True
_template_filename = '/var/www/dev/Candor/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['navigation', 'title', 'footer', 'content']


from django_mako_plus.controller import static_files 

from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navigation():
            return render_navigation(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        environment = context.get('environment', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n<head>\n    <meta charset="UTF-8">\n    <meta name="description" content="Candor Contracts strives to provide the easiest way to buy and sell apartment contracts, making a student\'s life much less hectic.">\n    <meta name="keywords" content="Candor, Candor Contracts, contract, contracts, apartment, apartment contracts, student, students">\n    <meta name="author" content="Daniel Wyatt">\n    \n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n    <link type="image/png" rel="icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/logo.png">\n    \n')
        __M_writer('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>\n    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/jquery.form.js"></script>\n\n    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" rel="stylesheet">\n    \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n\n</head>\n<body cz-shortcut-listen="true" id="home">\n  \n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation'):
            context['self'].navigation(**pageargs)
        

        __M_writer('\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navigation():
            return render_navigation(context)
        environment = context.get('environment', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('            <nav class="navbar navbar-default">\n                <div class="container">\n                    <!-- Brand and toggle get grouped for better mobile display -->\n                    <div class="navbar-header">\n                        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                            <span class="sr-only">Toggle navigation</span>\n                            <span class="icon-bar"></span>\n                            <span class="icon-bar"></span>\n                            <span class="icon-bar"></span>\n                        </button>\n                        <a class="navbar-brand" href="/"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/candor.png" />\n')
        if environment != '/var/www/candor':
            __M_writer('                                Candor Contracts Dev\n')
        else:
            __M_writer('                                Candor Contracts\n')
        __M_writer('                        </a>\n                    </div>\n\n                    <!-- Collect the nav links, forms, and other content for toggling -->\n                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                        <ul class="nav navbar-nav">\n                            <!-- <li><a href="#">Link <span class="sr-only">(current)</span></a></li>\n                            <li><a href="#">Link</a></li>\n                            <li class="dropdown">\n                                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\n                                <ul class="dropdown-menu" role="menu">\n                                    <li><a href="#">Action</a></li>\n                                    <li><a href="#">Another action</a></li>\n                                    <li><a href="#">Something else here</a></li>\n                                    <li class="divider"></li>\n                                    <li><a href="#">Separated link</a></li>\n                                    <li class="divider"></li>\n                                    <li><a href="#">One more separated link</a></li>\n                                </ul>\n                            </li> -->\n                        </ul>\n                        <ul class="nav navbar-nav navbar-right">\n                            <!-- <li><a href="#">Link</a></li>\n                            <li class="dropdown">\n                                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\n                                <ul class="dropdown-menu" role="menu">\n                                    <li><a href="#">Action</a></li>\n                                    <li><a href="#">Another action</a></li>\n                                    <li><a href="#">Something else here</a></li>\n                                    <li class="divider"></li>\n                                    <li><a href="#">Separated link</a></li>\n                                </ul>\n                            </li> -->\n                            <li><a href="#home">Home</a></li>\n                            <li><a href="#about">About</a></li>\n                            <li><a href="#contact">Contact</a></li>\n')
        __M_writer('                        </ul>\n                    </div><!-- /.navbar-collapse -->\n                </div><!-- /.container-fluid -->\n            </nav>\n')
        __M_writer('    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n        <title>homepage</title>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n        <footer>\n            Copyright &copy; ')
        __M_writer(str( datetime.now().year ))
        __M_writer(' Candor Contracts\n        </footer>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n        Site content goes here in sub-templates.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "source_encoding": "utf-8", "filename": "/var/www/dev/Candor/homepage/templates/base.htm", "line_map": {"131": 102, "137": 102, "143": 137, "16": 4, "18": 7, "20": 0, "37": 2, "38": 4, "39": 5, "43": 5, "44": 7, "49": 19, "50": 21, "51": 21, "52": 24, "53": 27, "54": 27, "55": 32, "56": 32, "57": 32, "62": 100, "67": 104, "72": 110, "73": 113, "74": 113, "75": 113, "81": 38, "89": 38, "90": 40, "91": 50, "92": 50, "93": 51, "94": 52, "95": 53, "96": 54, "97": 56, "98": 95, "99": 100, "105": 17, "111": 17, "117": 106, "123": 106, "124": 108, "125": 108}}
__M_END_METADATA
"""

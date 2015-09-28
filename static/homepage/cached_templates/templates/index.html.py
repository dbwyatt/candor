# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434867245.2071068
_enable_loop = True
_template_filename = '/var/www/dev/Candor/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


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
        contact = context.get('contact', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        csrf_token = context.get('csrf_token', UNDEFINED)
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        csrf_token = context.get('csrf_token', UNDEFINED)
        contact = context.get('contact', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div id="main-container">\n\t\t<div class="home-background"></div>\n\t\t<div class="overlay">\n\t\t\t<span id="coming-soon">coming soon</span>\n\t\t\t<div id="candor-container">\n\t\t\t\t<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/candor.png" />\n\t\t\t\t<span id="candor">Candor</span>\n\t\t\t\t<span id="contracts">Contracts</span>\n\t\t\t</div>\n\t\t\t<span class="space"></span>\n\t\t\t<!-- <form id="sign-up" method="POST" action="/homepage/index.register/">\n\t\t\t\t<label>Sign up for early registration</label>\n\t\t\t\t<span><input type="text" name="firstname" id="first-name" placeholder="First Name"/></span>\n\t\t\t\t<span><input type="text" name="lastname" id="last-name" placeholder="Last Name" /></span>\n\t\t\t\t<span><input type="email" name="email" id="email" placeholder="Email" /></span>\n\t\t\t\t<sup>*Your email will not be used for anything other than to contact you when Candor is ready to be tested</sup>\n\t\t\t\t<input type="submit" class="btn btn-primary" value="Sign Up" />\n\t\t\t</form> -->\n\t\t\t<form id="sign-up" method="POST" action="/homepage/index.register/">\n\t\t\t\t<label>Sign up for early registration</label>\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t\t\t\t<sup>*Your email will not be used for anything other than to contact you when Candor is ready to be tested</sup>\n\t\t\t\t<input type="submit" class="btn btn-primary" value="Sign Up" />\n\t\t\t\t<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(str( csrf_token ))
        __M_writer('\' />\n\t\t\t</form>\n\t\t</div>\n\t</div>\n\n\t<div class="page-panel blue">\n\t\t<div id="about" class="container">\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\t<h2 class="page-header">Welcome to Candor!</h2>\n\n\t\t\t\tCandor is a platform that strives to deliver the greatest, simplest, most beautiful way to escape or find your apartment contract. Candor started because one afternoon two students were trying to solve a problem that they themselves had dealt with, along with many of their friends.\n\n')
        __M_writer('\t\t\t</div>\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\t<iframe width="560" height="315" src="https://www.youtube.com/embed/UkDhSjSuJfM" frameborder="0" allowfullscreen></iframe>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n\t<div class="page-panel white">\n\t\t<div id="meet-us">\n\t\t\t<div class="col-sm-12 col-md-3">\n\t\t\t\t<div class="founder">\n\t\t\t\t\t<div class="founder-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bruce_peck.jpg\')"></div>\n\t\t\t\t\t<div class="founder-description">\n\t\t\t\t\t\t<span class="name">Bruce Peck</span>\n\t\t\t\t\t\t<span class="title">Co-Founder and Marketing</span>\n\t\t\t\t\t\tThis is Bruce. He is awesome! He has a huge passion for helping solve students problems and wants to do everything he can to make this project succeed. Bruce has backgrounds in entrepenuership and marketing which he uses to help push this project along. He has created great relationships with many individuals and apartment complexes in relation to Candor.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="col-sm-12 col-md-3">\n\t\t\t\t<div class="founder">\t\n\t\t\t\t\t<div class="founder-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/daniel.jpg\')"></div>\n\t\t\t\t\t<div class="founder-description">\n\t\t\t\t\t\t<span class="name">Daniel Wyatt</span>\n\t\t\t\t\t\t<span class="title">Co-Founder and Development</span>\n\t\t\t\t\t\tDaniel is currently a student at BYU and handles the development of this project. He loves being part of something where he can use his skills to help fellow students. Daniel has backgrounds in business and development.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n\t<div class="page-panel off">\n\t\t<div id="contact" class="container">\n\t\t\t<h2 class="page-header">Contact Us</h2>\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\tWe would love to hear from you! If you have a great idea that would help you to sell your contract easier or just want to say hi, send us a message.\n\t\t\t\t<br><br>\n\t\t\t\t<b>Email</b> - <a href="mailto:candorcontracts@gmail.com">candorcontracts@gmail.com</a>\n\t\t\t\t<br>\n\t\t\t\t<b>Phone</b> - (801) 960-2140\n\t\t\t</div>\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\t<form id="contact-form" method="POST" action="/homepage/index.contact/">\n\t\t\t\t\t<label>Send us a message here</label>\n\t\t\t\t\t')
        __M_writer(str( contact ))
        __M_writer('\n')
        __M_writer('\t\t\t\t\t<input type="submit" class="btn btn-primary" value="Send" />\n\t\t\t\t\t<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(str( csrf_token ))
        __M_writer("' />\n\t\t\t\t</form>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n\t<title>Candor Contracts</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "source_encoding": "utf-8", "line_map": {"65": 7, "66": 14, "67": 14, "68": 29, "69": 29, "70": 32, "71": 32, "72": 63, "73": 74, "74": 74, "75": 84, "76": 84, "77": 108, "78": 108, "79": 110, "80": 111, "81": 111, "87": 3, "27": 0, "93": 3, "99": 93, "40": 1, "45": 5, "55": 7}, "filename": "/var/www/dev/Candor/homepage/templates/index.html"}
__M_END_METADATA
"""

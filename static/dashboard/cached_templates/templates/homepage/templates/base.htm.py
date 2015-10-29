# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446092057.737841
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['navigation', 'content', 'footer', 'login', 'title', 'rightlinks']


from django_mako_plus.controller import static_files 

from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navigation():
            return render_navigation(context._locals(__M_locals))
        environment = context.get('environment', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def login():
            return render_login(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def rightlinks():
            return render_rightlinks(context._locals(__M_locals))
        csrf_token = context.get('csrf_token', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <meta name="description" content="Candor Contracts strives to provide the easiest way to buy and sell apartment contracts, making a student\'s life much less hectic.">\r\n    <meta name="keywords" content="Candor, Candor Contracts, contract, contracts, apartment, apartment contracts, student, students">\r\n    <meta name="author" content="Daniel Wyatt">\r\n    <meta name="google-signin-client_id" content="267671914850-gtsdijk1ela2bc5076t6alla50m2t2ad.apps.googleusercontent.com">\r\n    \r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n    <link type="image/png" rel="icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/logo.png">\r\n    \r\n')
        __M_writer('    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>\r\n    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/jquery.form.js"></script>\r\n    <script src="https://apis.google.com/js/api:client.js"></script>\r\n\r\n    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" rel="stylesheet">\r\n    <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/font-awesome.css" />\r\n    \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n\r\n</head>\r\n<body cz-shortcut-listen="true" id="home">\r\n\r\n    <div id="fb-root"></div>\r\n    <script>\r\n        window.fbAsyncInit = function() {\r\n            FB.init({\r\n                appId      : \'1639785522934996\',\r\n                xfbml      : true,\r\n                version    : \'v2.3\'\r\n            });\r\n        };\r\n\r\n        (function(d, s, id){\r\n            var js, fjs = d.getElementsByTagName(s)[0];\r\n            if (d.getElementById(id)) {return;}\r\n            js = d.createElement(s); js.id = id;\r\n            js.src = "//connect.facebook.net/en_US/sdk.js";\r\n            fjs.parentNode.insertBefore(js, fjs);\r\n        }(document, \'script\', \'facebook-jssdk\'));\r\n    </script>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation'):
            context['self'].navigation(**pageargs)
        

        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login'):
            context['self'].login(**pageargs)
        

        __M_writer('\r\n\r\n    <script>\r\n        function onSignIn(googleUser, element) {\r\n            $(element).append(\'<i class="fa fa-spinner fa-fw fa-spin"></i>\');\r\n            var profile = googleUser.getBasicProfile();\r\n            var scopes = googleUser.getGrantedScopes();\r\n            // console.log(\'ID: \' + profile.getId()); // Do not send to your backend! Use an ID token instead.\r\n            // console.log(\'Name: \' + profile.getName());\r\n            // console.log(\'Image URL: \' + profile.getImageUrl());\r\n            // console.log(\'Email: \' + profile.getEmail());\r\n            // $(\'.sign-in\').text(\'Welcome, \' + profile.getName());\r\n            // $(\'#login-slide .close\').trigger(\'click\');\r\n            $.ajax({\r\n                type: \'POST\',\r\n                url: \'/homepage/\',\r\n                data: {set: true, csrfmiddlewaretoken: $(\'[name="csrfmiddlewaretoken"]\').val(), name: profile.getName(), image: profile.getImageUrl(), email: profile.getEmail(), id_token: googleUser.getAuthResponse().id_token},\r\n                success: function(ret) {\r\n                    if (ret == \'True\') {\r\n                        window.location = \'/dashboard/\';\r\n                    }\r\n                },\r\n                error: function(e) {\r\n                    console.log(e);\r\n                }\r\n            });\r\n        }\r\n\r\n        function signOut() {\r\n            var auth2 = gapi.auth2.getAuthInstance();\r\n            auth2.signOut().then(function () {\r\n                console.log(\'User signed out.\');\r\n                $.ajax({\r\n                    type: \'POST\',\r\n                    url: \'/homepage/\',\r\n                    data: {set: false, csrfmiddlewaretoken: $(\'[name="csrfmiddlewaretoken"]\').val()},\r\n                    success: function(ret) {\r\n                        if (ret == \'True\') {\r\n                            window.location = \'/homepage/\';\r\n                        }\r\n                    },\r\n                    error: function(e) {\r\n                        console.log(e);\r\n                    }\r\n                });\r\n            });\r\n        }\r\n\r\n        var googleUser = {};\r\n        var startApp = function() {\r\n            gapi.load(\'auth2\', function() {\r\n                // Retrieve the singleton for the GoogleAuth library and set up the client.\r\n                auth2 = gapi.auth2.init({\r\n                    client_id: \'267671914850-gtsdijk1ela2bc5076t6alla50m2t2ad.apps.googleusercontent.com\',\r\n                    cookiepolicy: \'single_host_origin\',\r\n                    // Request scopes in addition to \'profile\' and \'email\'\r\n                    scope: \'profile email https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/plus.login\'\r\n                });\r\n                attachSignin(document.getElementById(\'my-signin2\'));\r\n            })\r\n        }\r\n\r\n        function attachSignin(element) {\r\n            // console.log(element.id);\r\n            auth2.attachClickHandler(element, {},\r\n                function(googleUser) {\r\n                    onSignIn(googleUser, element);\r\n                },\r\n                function(error) {\r\n                    // alert(JSON.stringify(error, undefined, 2));\r\n                }\r\n            );\r\n        }\r\n\r\n        startApp();\r\n    </script>\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def rightlinks():
            return render_rightlinks(context)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def navigation():
            return render_navigation(context)
        environment = context.get('environment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('            <nav class="navbar navbar-default navbar-fixed-top">\r\n                <div class="container">\r\n                    <!-- Brand and toggle get grouped for better mobile display -->\r\n                    <div class="navbar-header">\r\n                        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n                            <span class="sr-only">Toggle navigation</span>\r\n                            <span class="icon-bar"></span>\r\n                            <span class="icon-bar"></span>\r\n                            <span class="icon-bar"></span>\r\n                        </button>\r\n                        <a class="navbar-brand" href="/"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/candor.png" />\r\n                            <span class="brand-text">\r\n')
        if environment != '/var/www/candor':
            __M_writer('                                    Candor Contracts Dev\r\n')
        else:
            __M_writer('                                    Candor Contracts\r\n')
        __M_writer('                            </span>\r\n                        </a>\r\n                    </div>\r\n\r\n                    <!-- Collect the nav links, forms, and other content for toggling -->\r\n                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                        <ul class="nav navbar-nav">\r\n                            <!-- <li><a href="#">Link <span class="sr-only">(current)</span></a></li>\r\n                            <li><a href="#">Link</a></li>\r\n                            <li class="dropdown">\r\n                                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\r\n                                <ul class="dropdown-menu" role="menu">\r\n                                    <li><a href="#">Action</a></li>\r\n                                    <li><a href="#">Another action</a></li>\r\n                                    <li><a href="#">Something else here</a></li>\r\n                                    <li class="divider"></li>\r\n                                    <li><a href="#">Separated link</a></li>\r\n                                    <li class="divider"></li>\r\n                                    <li><a href="#">One more separated link</a></li>\r\n                                </ul>\r\n                            </li> -->\r\n                            <li class="social-links">\r\n                                <a class="social" target="_blank" href="https://www.facebook.com/candorcontracts"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/facebook.png" /></a>\r\n                                <a class="social" target="_blank" href="https://plus.google.com/113660936428650731143/posts"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/google-plus.png" /></a>\r\n                                <a class="social" target="_blank" href="https://www.youtube.com/channel/UCXyFif0645OPd5TZvynb-sQ"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/youtube.png" /></a>\r\n                            </li>\r\n                        </ul>\r\n                        <ul class="nav navbar-nav navbar-right">\r\n                            <!-- <li><a href="#">Link</a></li>\r\n                            <li class="dropdown">\r\n                                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Dropdown <span class="caret"></span></a>\r\n                                <ul class="dropdown-menu" role="menu">\r\n                                    <li><a href="#">Action</a></li>\r\n                                    <li><a href="#">Another action</a></li>\r\n                                    <li><a href="#">Something else here</a></li>\r\n                                    <li class="divider"></li>\r\n                                    <li><a href="#">Separated link</a></li>\r\n                                </ul>\r\n                            </li> -->\r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'rightlinks'):
            context['self'].rightlinks(**pageargs)
        

        __M_writer('\r\n')
        if 'user' not in request.session:
            __M_writer('                                <li><a href="#" class="sign-in">Sign In</a></li>\r\n')
        else:
            __M_writer('                                <li class="dropdown">\r\n                                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="name">Hello, ')
            __M_writer(str( request.session['user']['name'][0] ))
            __M_writer('</span><span class="account">Your Account</span> <span class="caret"></span></a>\r\n                                    <ul class="dropdown-menu" role="menu">\r\n                                        <li><a href="/dashboard/"><i class="fa fa-dashboard fa-fw"></i>Dashboard</a></li>\r\n                                        <li class="divider"></li>\r\n                                        <li><a href="/accounts/"><i class="fa fa-user fa-fw"></i>Account</a></li>\r\n                                        <li class="divider"></li>\r\n                                        <li><a href="#" onclick=signOut()><i class="fa fa-sign-out fa-fw"></i>Logout</a></li>\r\n                                    </ul>\r\n                                </li>\r\n')
        __M_writer('                        </ul>\r\n                    </div><!-- /.navbar-collapse -->\r\n                </div><!-- /.container-fluid -->\r\n            </nav>\r\n')
        __M_writer('    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n        Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <footer>\r\n            Copyright &copy; ')
        __M_writer(str( datetime.now().year ))
        __M_writer(' Candor Contracts\r\n        </footer>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login():
            return render_login(context)
        csrf_token = context.get('csrf_token', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n        <form id="set-user" style="display: none;">\r\n            <input type="submit" />\r\n            <input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(str( csrf_token ))
        __M_writer("' />\r\n        </form>\r\n    ")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <title>Candor Contracts - Homepage</title>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_rightlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def rightlinks():
            return render_rightlinks(context)
        __M_writer = context.writer()
        __M_writer('\r\n                                <li><a href="/">Home</a></li>\r\n                                <li><a href="/#about">About</a></li>\r\n                                <li><a href="/#contact">Contact</a></li>\r\n                            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"128": 127, "129": 127, "130": 138, "131": 143, "137": 145, "190": 118, "143": 145, "16": 4, "18": 7, "171": 158, "20": 0, "149": 149, "202": 196, "155": 149, "156": 151, "157": 151, "163": 155, "42": 2, "43": 4, "44": 5, "48": 5, "49": 7, "178": 18, "172": 158, "54": 20, "55": 22, "56": 22, "57": 25, "58": 28, "59": 28, "60": 32, "61": 32, "62": 35, "63": 35, "64": 35, "196": 118, "69": 143, "74": 147, "79": 153, "184": 18, "84": 160, "85": 237, "86": 237, "87": 237, "93": 60, "104": 60, "105": 62, "106": 72, "107": 72, "108": 74, "109": 75, "110": 76, "111": 77, "112": 79, "113": 101, "114": 101, "115": 102, "116": 102, "117": 103, "118": 103, "170": 155, "123": 122, "124": 123, "125": 124, "126": 125, "127": 126}, "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor/homepage/templates/base.htm"}
__M_END_METADATA
"""

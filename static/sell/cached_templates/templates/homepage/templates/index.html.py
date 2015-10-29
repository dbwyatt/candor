# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1443826506.135223
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor/homepage/templates/index.html'
_template_uri = '/homepage/templates/index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content']


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
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        csrf_token = context.get('csrf_token', UNDEFINED)
        request = context.get('request', UNDEFINED)
        contact = context.get('contact', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        csrf_token = context.get('csrf_token', UNDEFINED)
        request = context.get('request', UNDEFINED)
        contact = context.get('contact', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<div id="main-container">\r\n\t\t<div class="home-background"></div>\r\n\t\t<div class="overlay">\r\n')
        __M_writer('\t\t\t<div id="candor-container">\r\n\t\t\t\t<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/candor.png" />\r\n\t\t\t\t<span id="candor">Candor</span>\r\n\t\t\t\t<span id="contracts">Contracts</span>\r\n\t\t\t</div>\r\n')
        __M_writer('\t\t\t<!-- <form id="sign-up" method="POST" action="/homepage/index.register/">\r\n\t\t\t\t<label>Sign up for early registration</label>\r\n\t\t\t\t<span><input type="text" name="firstname" id="first-name" placeholder="First Name"/></span>\r\n\t\t\t\t<span><input type="text" name="lastname" id="last-name" placeholder="Last Name" /></span>\r\n\t\t\t\t<span><input type="email" name="email" id="email" placeholder="Email" /></span>\r\n\t\t\t\t<sup>*Your email will not be used for anything other than to contact you when Candor is ready to be tested</sup>\r\n\t\t\t\t<input type="submit" class="btn btn-primary" value="Sign Up" />\r\n\t\t\t</form> -->\r\n')
        __M_writer('\t\t\t<span class="freedom">Freedom is just around the corner</span>\r\n')
        if 'user' not in request.session:
            __M_writer('\t\t\t\t<a href="#" class="start-here">Start Here</a>\r\n')
        else:
            __M_writer('\t\t\t\t<a href="/dashboard/" class="start-here">Start Here</a>\r\n')
        __M_writer('\r\n')
        if 'user' not in request.session:
            __M_writer('\t\t\t\t<div id="login-slide">\r\n\t                <link type="text/css" rel="stylesheet" href="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/styles/bootstrap-social.css" />\r\n\t\t\t\t\t<div class="close">x</div>\r\n\r\n\t\t\t\t\t<div id="login-container">\r\n\t\t\t\t\t\t<span class="login-text">Login with your Google or Facebook account</span>\r\n\t\t\t\t\t\t<div class="btn-wrapper">\t\r\n\t\t\t\t\t\t\t<div id="my-signin2" class="btn btn-block btn-social btn-google" data-onsuccess="onSignIn">\r\n\t\t\t\t\t\t\t\t<i class="fa fa-google"></i> Sign in with Google\r\n\t\t\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t\t\t<span class="spacer"></span>\r\n\r\n\t\t\t\t\t\t\t<a class="btn btn-block btn-social btn-facebook" data-onsuccess="onSignIn">\r\n\t\t\t\t\t\t\t\t<i class="fa fa-facebook"></i> Sign in with Facebook\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\r\n')
            __M_writer('\r\n\t\t\t\t</div>\r\n')
        __M_writer('\t\t</div>\r\n\t</div>\r\n\r\n\t<div class="page-panel blue">\r\n\t\t<div id="about" class="container">\r\n\t\t\t<div class="col-sm-12 col-md-6">\r\n\t\t\t\t<h2 class="page-header">What is Candor</h2>\r\n\r\n')
        __M_writer('\r\n\t\t\t\tCandor is a tinder like website for college students and apartment complexes to buy and sell their apartment contracts, faster and easier than it has ever been before. \r\n\t\t\t\t<br><br>\r\n\t\t\t\tThe Story of Candor: \r\n\t\t\t\t<br><br>\r\n\t\t\t\tLet’s go back to the fall of 2014, shall we? Bruce’s roommate, we’ll call him Skyler (because that is his name) was literally yelling at his tablet. Why was he yelling at his tablet you ask? Because he had just paid 10$ to a website (which we will call notcandorcontracts.com)  that didn’t work to try to sell his apartment contract...and he wasn’t getting his money back. “I wonder what would happen if we built a website that actually sold your contract really fast?” thought Bruce. So more than six months, a business competition or two and hours of blood and sweat and toil later, we present to you,\r\n\t\t\t\t<br><br>\r\n\t\t\t\tCandor.\r\n\t\t\t\t<br><br>\r\n\t\t\t\tPs: Now would be an appropriate time to let out an “ooo” or an “ahhh”\r\n\t\t\t</div>\r\n\t\t\t<div class="col-sm-12 col-md-6">\r\n\t\t\t\t<iframe width="560" height="315" src="https://www.youtube.com/embed/UkDhSjSuJfM" frameborder="0" allowfullscreen></iframe>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n\r\n\t<div class="page-panel white">\r\n\t\t<div class="container">\r\n\t\t\t<div class="col-sm-12 col-md-6">\r\n\t\t\t</div>\r\n\t\t\t<div class="col-sm-12 col-md-6">\r\n\t\t\t\t<h2 class="page-header">Sell within days instead of weeks</h2>\r\n\t\t\t</div>\r\n\t\t\t<div class="list-container">\r\n\t\t\t\t<div class="list-item">\r\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/facebook-128 (1).png\')"></div>\r\n\t\t\t\t\t<div class="list-item-description">\r\n\t\t\t\t\t\t<span class="title">Post to where you need</span>\r\n\t\t\t\t\t\tPost to KSL, Craigslist, and Facebook all from one easy location all at the same time for free. People will be redirected from those sites back to your posting for easy central access to everything that\'s going on with your contract.\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="list-item">\r\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/conference-128 (1).png\')"></div>\r\n\t\t\t\t\t<div class="list-item-description">\r\n\t\t\t\t\t\t<span class="title">Get seen by the right people</span>\r\n\t\t\t\t\t\tBy partnering with apartment complexes, blogs, Facebook groups and others, Candor provides focused traffic of people that actually want to buy your contract. We work hard to find the people, so you, my friend, don’t have to.\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="list-item">\r\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/message-2-128 (1).png\')"></div>\r\n\t\t\t\t\t<div class="list-item-description">\r\n\t\t\t\t\t\t<span class="title">Easy messaging</span>\r\n\t\t\t\t\t\tCandor allows for very simple messaging between you and the buyer, no need to exchange phone numbers or email addresses. And, Candor let’s you know how interested the buyer is on a scale of 1 to 10 (wouldn’t that feature be nice for dating…).\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="list-item">\r\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/speed-128 (1).png\')"></div>\r\n\t\t\t\t\t<div class="list-item-description">\r\n\t\t\t\t\t\t<span class="title">Speed up the process</span>\r\n\t\t\t\t\t\tCandor Pro allows you to search out people who are looking for your type of contract and message them proactively. It also allows you to set up an incentive for someone to buy your contract (ex. paying for first month’s rent) and post a video of a tour of your apartment to set you apart.\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n\r\n\t<div class="page-panel off">\r\n\t\t<div class="container">\r\n\t\t\t<div class="col-sm-12 col-md-6">\r\n\t\t\t\t<h2 class="page-header">Find available contracts instantly</h2>\r\n\t\t\t</div>\r\n\t\t\t<div class="col-sm-12 col-md-6">\r\n\t\t\t</div>\r\n\t\t\t<div class="list-container">\r\n\t\t\t\t<div class="list-item">\r\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/paper-128.png\')"></div>\r\n\t\t\t\t\t<div class="list-item-description">\r\n\t\t\t\t\t\t<span class="title">Find the perfect contract for you</span>\r\n\t\t\t\t\t\tWhether you want to get into an apartment complex that is full (perhaps to live a bit closer to you know who), find a deal on a contract (if you need a little extra Ramen money) or get a contract at an odd time of the year, Candor can help you out.\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="list-item">\r\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/horizontal-swipe-128.png\')"></div>\r\n\t\t\t\t\t<div class="list-item-description">\r\n\t\t\t\t\t\t<span class="title">Simple, easy, and beautiful</span>\r\n\t\t\t\t\t\tCandor is the swiss army knife of apartment websites. No more searching through dozens of websites, writing comparison charts, calling to see what available or trying to manually narrow down options. Candor does it for you, just say what you\'re looking for, and swipe left till you find it.\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="list-item">\r\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/checked-user-128.png\')"></div>\r\n\t\t\t\t\t<div class="list-item-description">\r\n\t\t\t\t\t\t<span class="title">Know what you\'re getting into</span>\r\n\t\t\t\t\t\tAKA no more scammers! Candor partners with apartment complexes and can verify if the person selling the contract is real or fake, therefore, we will only show you the real ones. Also know what your new apartment expects of you by  seeing the rules associated with each complex.\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n\r\n\t<div class="page-panel white">\r\n\t\t<div id="meet-us">\r\n\t\t\t<div class="col-sm-12 col-md-3">\r\n\t\t\t\t<div class="founder">\r\n\t\t\t\t\t<div class="founder-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bruce_peck.jpg\')"></div>\r\n\t\t\t\t\t<div class="founder-description">\r\n\t\t\t\t\t\t<span class="name">Bruce Peck</span>\r\n\t\t\t\t\t\t<span class="title">Co-Founder and Marketing</span>\r\n\t\t\t\t\t\tThis is Bruce. He is awesome! He has a huge passion for helping solve students problems and wants to do everything he can to make this project succeed. Bruce has backgrounds in entrepenuership and marketing which he uses to help push this project along. He has created great relationships with many individuals and apartment complexes in relation to Candor.\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<div class="col-sm-12 col-md-3">\r\n\t\t\t\t<div class="founder">\t\r\n\t\t\t\t\t<div class="founder-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/daniel.jpg\')"></div>\r\n\t\t\t\t\t<div class="founder-description">\r\n\t\t\t\t\t\t<span class="name">Daniel Wyatt</span>\r\n\t\t\t\t\t\t<span class="title">Co-Founder and Development</span>\r\n\t\t\t\t\t\tThis is Daniel and he is likewise awesome. We became business partners thanks to the internet. He’s a student at BYU and a father of one kid and also this website. He is an Information Systems major and knows how to make coding magic happen. When your contract sells due to Candor you can thank him, if it doesn’t, well, you can talk to me.\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n\r\n\t<div class="page-panel off">\r\n\t\t<div id="contact" class="container">\r\n\t\t\t<h2 class="page-header">Contact Us</h2>\r\n\t\t\t<div class="col-sm-12 col-md-6">\r\n\t\t\t\tWe would love to hear from you! If you have a great idea that would help you to sell your contract easier or just want to say hi, send us a message. This may look like a normal contact us form, but it’s not, because we actually want you to contact us. Seriously. Give us a call or send us a message.\r\n\t\t\t\t<br><br>\r\n\t\t\t\t<b>Email</b> - <a href="mailto:candorcontracts@gmail.com">candorcontracts@gmail.com</a>\r\n\t\t\t\t<br>\r\n\t\t\t\t<b>Phone</b> - (801) 960-2140\r\n\t\t\t</div>\r\n\t\t\t<div class="col-sm-12 col-md-6">\r\n\t\t\t\t<form id="contact-form" method="POST" action="/homepage/index.contact/">\r\n\t\t\t\t\t<label>Send us a message here</label>\r\n\t\t\t\t\t')
        __M_writer(str( contact ))
        __M_writer('\r\n')
        __M_writer('\t\t\t\t\t<input type="submit" class="btn btn-primary" value="Send" />\r\n\t\t\t\t\t<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(str( csrf_token ))
        __M_writer("' />\r\n\t\t\t\t</form>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor/homepage/templates/index.html", "line_map": {"27": 0, "40": 1, "45": 5, "55": 3, "61": 3, "67": 7, "77": 7, "78": 13, "79": 14, "80": 14, "81": 19, "82": 34, "83": 35, "84": 36, "85": 37, "86": 38, "87": 40, "88": 41, "89": 42, "90": 43, "91": 43, "92": 63, "93": 66, "94": 75, "95": 101, "96": 101, "97": 108, "98": 108, "99": 115, "100": 115, "101": 122, "102": 122, "103": 141, "104": 141, "105": 148, "106": 148, "107": 155, "108": 155, "109": 169, "110": 169, "111": 179, "112": 179, "113": 203, "114": 203, "115": 205, "116": 206, "117": 206, "123": 117}, "uri": "/homepage/templates/index.html"}
__M_END_METADATA
"""

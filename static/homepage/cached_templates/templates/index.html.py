# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1435814979.6790116
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
        def content():
            return render_content(context._locals(__M_locals))
        contact = context.get('contact', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        csrf_token = context.get('csrf_token', UNDEFINED)
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
        def content():
            return render_content(context)
        contact = context.get('contact', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        csrf_token = context.get('csrf_token', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div id="main-container">\n\t\t<div class="home-background"></div>\n\t\t<div class="overlay">\n')
        __M_writer('\t\t\t<div id="candor-container">\n\t\t\t\t<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/candor.png" />\n\t\t\t\t<span id="candor">Candor</span>\n\t\t\t\t<span id="contracts">Contracts</span>\n\t\t\t</div>\n')
        __M_writer('\t\t\t<!-- <form id="sign-up" method="POST" action="/homepage/index.register/">\n\t\t\t\t<label>Sign up for early registration</label>\n\t\t\t\t<span><input type="text" name="firstname" id="first-name" placeholder="First Name"/></span>\n\t\t\t\t<span><input type="text" name="lastname" id="last-name" placeholder="Last Name" /></span>\n\t\t\t\t<span><input type="email" name="email" id="email" placeholder="Email" /></span>\n\t\t\t\t<sup>*Your email will not be used for anything other than to contact you when Candor is ready to be tested</sup>\n\t\t\t\t<input type="submit" class="btn btn-primary" value="Sign Up" />\n\t\t\t</form> -->\n')
        __M_writer('\t\t\t<span class="freedom">Freedom is just around the corner</span>\n\t\t\t<button class="start-here">Start Here</button>\n\t\t\t<div id="login-slide">\n                <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/font-awesome.css" />\n                <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/bootstrap-social.css" />\n\t\t\t\t<div class="close">x</div>\n\n\t\t\t\t<div id="login-container">\n\t\t\t\t\t<span class="login-text">Login with your Google or Facebook account</span>\n\t\t\t\t\t<div class="btn-wrapper">\t\n\t\t\t\t\t\t<div class="btn btn-block btn-social btn-google" data-onsuccess="onSignIn">\n\t\t\t\t\t\t\t<i class="fa fa-google"></i> Sign in with Google\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n\t\t\t\t\t\t<span class="spacer"></span>\n\n\t\t\t\t\t\t<a class="btn btn-block btn-social btn-facebook" data-onsuccess="onSignIn">\n\t\t\t\t\t\t\t<i class="fa fa-facebook"></i> Sign in with Facebook\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\n')
        __M_writer('\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n\t<div class="page-panel blue">\n\t\t<div id="about" class="container">\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\t<h2 class="page-header">What is Candor</h2>\n\n')
        __M_writer('\n\t\t\t\tCandor is a tinder like website for college students and apartment complexes to buy and sell their apartment contracts, faster and easier than it has ever been before. \n\t\t\t\t<br><br>\n\t\t\t\tThe Story of Candor: \n\t\t\t\t<br><br>\n\t\t\t\tLet’s go back to the fall of 2014, shall we? Bruce’s roommate, we’ll call him Skyler (because that is his name) was literally yelling at his tablet. Why was he yelling at his tablet you ask? Because he had just paid 10$ to a website (which we will call notcandorcontracts.com)  that didn’t work to try to sell his apartment contract...and he wasn’t getting his money back. “I wonder what would happen if we built a website that actually sold your contract really fast?” thought Bruce. So more than six months, a business competition or two and hours of blood and sweat and toil later, we present to you,\n\t\t\t\t<br><br>\n\t\t\t\tCandor.\n\t\t\t\t<br><br>\n\t\t\t\tPs: Now would be an appropriate time to let out an “ooo” or an “ahhh”\n\t\t\t</div>\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\t<iframe width="560" height="315" src="https://www.youtube.com/embed/UkDhSjSuJfM" frameborder="0" allowfullscreen></iframe>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n\t<div class="page-panel white">\n\t\t<div class="container">\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t</div>\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\t<h2 class="page-header">Sell within days instead of weeks</h2>\n\t\t\t</div>\n\t\t\t<div class="list-container">\n\t\t\t\t<div class="list-item">\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/facebook-128 (1).png\')"></div>\n\t\t\t\t\t<div class="list-item-description">\n\t\t\t\t\t\t<span class="title">Post to where you need</span>\n\t\t\t\t\t\tPost to KSL, Craigslist, and Facebook all from one easy location all at the same time for free. People will be redirected from those sites back to your posting for easy central access to everything that\'s going on with your contract.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="list-item">\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/conference-128 (1).png\')"></div>\n\t\t\t\t\t<div class="list-item-description">\n\t\t\t\t\t\t<span class="title">Get seen by the right people</span>\n\t\t\t\t\t\tBy partnering with apartment complexes, blogs, Facebook groups and others, Candor provides focused traffic of people that actually want to buy your contract. We work hard to find the people, so you, my friend, don’t have to.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="list-item">\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/message-2-128 (1).png\')"></div>\n\t\t\t\t\t<div class="list-item-description">\n\t\t\t\t\t\t<span class="title">Easy messaging</span>\n\t\t\t\t\t\tCandor allows for very simple messaging between you and the buyer, no need to exchange phone numbers or email addresses. And, Candor let’s you know how interested the buyer is on a scale of 1 to 10 (wouldn’t that feature be nice for dating…).\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="list-item">\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/speed-128 (1).png\')"></div>\n\t\t\t\t\t<div class="list-item-description">\n\t\t\t\t\t\t<span class="title">Speed up the process</span>\n\t\t\t\t\t\tCandor Pro allows you to search out people who are looking for your type of contract and message them proactively. It also allows you to set up an incentive for someone to buy your contract (ex. paying for first month’s rent) and post a video of a tour of your apartment to set you apart.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n\t<div class="page-panel off">\n\t\t<div class="container">\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\t<h2 class="page-header">Find available contracts instantly</h2>\n\t\t\t</div>\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t</div>\n\t\t\t<div class="list-container">\n\t\t\t\t<div class="list-item">\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/paper-128.png\')"></div>\n\t\t\t\t\t<div class="list-item-description">\n\t\t\t\t\t\t<span class="title">Find the perfect contract for you</span>\n\t\t\t\t\t\tWhether you want to get into an apartment complex that is full (perhaps to live a bit closer to you know who), find a deal on a contract (if you need a little extra Ramen money) or get a contract at an odd time of the year, Candor can help you out.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="list-item">\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/horizontal-swipe-128.png\')"></div>\n\t\t\t\t\t<div class="list-item-description">\n\t\t\t\t\t\t<span class="title">Simple, easy, and beautiful</span>\n\t\t\t\t\t\tCandor is the swiss army knife of apartment websites. No more searching through dozens of websites, writing comparison charts, calling to see what available or trying to manually narrow down options. Candor does it for you, just say what you\'re looking for, and swipe left till you find it.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="list-item">\n\t\t\t\t\t<div class="list-item-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/checked-user-128.png\')"></div>\n\t\t\t\t\t<div class="list-item-description">\n\t\t\t\t\t\t<span class="title">Know what you\'re getting into</span>\n\t\t\t\t\t\tAKA no more scammers! Candor partners with apartment complexes and can verify if the person selling the contract is real or fake, therefore, we will only show you the real ones. Also know what your new apartment expects of you by  seeing the rules associated with each complex.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n\t<div class="page-panel white">\n\t\t<div id="meet-us">\n\t\t\t<div class="col-sm-12 col-md-3">\n\t\t\t\t<div class="founder">\n\t\t\t\t\t<div class="founder-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bruce_peck.jpg\')"></div>\n\t\t\t\t\t<div class="founder-description">\n\t\t\t\t\t\t<span class="name">Bruce Peck</span>\n\t\t\t\t\t\t<span class="title">Co-Founder and Marketing</span>\n\t\t\t\t\t\tThis is Bruce. He is awesome! He has a huge passion for helping solve students problems and wants to do everything he can to make this project succeed. Bruce has backgrounds in entrepenuership and marketing which he uses to help push this project along. He has created great relationships with many individuals and apartment complexes in relation to Candor.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="col-sm-12 col-md-3">\n\t\t\t\t<div class="founder">\t\n\t\t\t\t\t<div class="founder-img" style="background-image:url(\'')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/daniel.jpg\')"></div>\n\t\t\t\t\t<div class="founder-description">\n\t\t\t\t\t\t<span class="name">Daniel Wyatt</span>\n\t\t\t\t\t\t<span class="title">Co-Founder and Development</span>\n\t\t\t\t\t\tThis is Daniel and he is likewise awesome. We became business partners thanks to the internet. He’s a student at BYU and a father of one kid and also this website. He is an Information Systems major and knows how to make coding magic happen. When your contract sells due to Candor you can thank him, if it doesn’t, well, you can talk to me.\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n\t<div class="page-panel off">\n\t\t<div id="contact" class="container">\n\t\t\t<h2 class="page-header">Contact Us</h2>\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\tWe would love to hear from you! If you have a great idea that would help you to sell your contract easier or just want to say hi, send us a message. This may look like a normal contact us form, but it’s not, because we actually want you to contact us. Seriously. Give us a call or send us a message.\n\t\t\t\t<br><br>\n\t\t\t\t<b>Email</b> - <a href="mailto:candorcontracts@gmail.com">candorcontracts@gmail.com</a>\n\t\t\t\t<br>\n\t\t\t\t<b>Phone</b> - (801) 960-2140\n\t\t\t</div>\n\t\t\t<div class="col-sm-12 col-md-6">\n\t\t\t\t<form id="contact-form" method="POST" action="/homepage/index.contact/">\n\t\t\t\t\t<label>Send us a message here</label>\n\t\t\t\t\t')
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
{"line_map": {"64": 13, "65": 14, "66": 14, "67": 19, "68": 34, "69": 37, "70": 37, "71": 38, "72": 38, "73": 58, "74": 69, "75": 95, "76": 95, "77": 102, "78": 102, "79": 109, "80": 109, "81": 116, "82": 116, "83": 135, "84": 135, "85": 142, "86": 142, "87": 149, "88": 149, "89": 163, "90": 163, "27": 0, "92": 173, "93": 197, "94": 197, "95": 199, "96": 200, "97": 200, "91": 173, "39": 1, "103": 3, "44": 5, "109": 3, "115": 109, "54": 7, "63": 7}, "filename": "/var/www/dev/Candor/homepage/templates/index.html", "source_encoding": "utf-8", "uri": "index.html"}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446092066.593826
_enable_loop = True
_template_filename = 'C:\\Users\\Daniel\\Documents\\Candor\\Candor\\sell\\templates/post.html'
_template_uri = 'post.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['footer', 'navigation', 'content']


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
        def navigation():
            return render_navigation(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        environment = context.get('environment', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        csrf_token = context.get('csrf_token', UNDEFINED)
        amenities = context.get('amenities', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        

        __M_writer('\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        csrf_token = context.get('csrf_token', UNDEFINED)
        amenities = context.get('amenities', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="main-container">\r\n\t\r\n\t\t')
        runtime._include_file(context, '/dashboard/templates/nav_stacked.html', _template_uri)
        __M_writer('\r\n\r\n\t\t<div id="action-container">\r\n\t\t\t<h1>Post a new contract</h1>\r\n\t\t\t<button class="btn btn-default prev">&#10094; Go back</button>\r\n\t\t\t<button class="btn btn-success next">Move on</button>\r\n\t\t\t<form id="post-form" method="POST" action="">\r\n\t\t\t\t<div class="post-input current" data-block="title" data-next="complex">\r\n\t\t\t\t\t<label class="question">What is the title of this post?</label>\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="title" id="title" />\r\n\t\t\t\t\t\t<span class="label-float">Title</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\r\n        <div class="post-input" data-block="complex" data-next="address">\r\n          <label class="question">What is the apartment complex?</label>\r\n          <div class="input-container">\r\n            <input type="text" name="complex" id="complex" />\r\n            <span class="label-float">Complex</span>\r\n          </div>\r\n        </div>\r\n\r\n\t\t\t\t<div class="post-input" data-block="address" data-next="description">\r\n\t\t\t\t\t<label class="question">What is the address?<br><sup>*For your own saftey we will not ask for exact apartment numbers</sup></label>\r\n\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="address1" id="address1" />\r\n\t\t\t\t\t\t<span class="label-float">Address 1</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="address2" id="address2" class="empty" />\r\n\t\t\t\t\t\t<span class="label-float">Address 2 <sup>(optional)</sup></span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="city" id="city" />\r\n\t\t\t\t\t\t<span class="label-float">City</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="input-container left col-2">\r\n\t\t\t\t\t\t<select name="state" id="state">\r\n\t\t\t\t\t\t\t<option></option>\r\n\t\t\t\t\t\t\t<option value="AL">Alabama</option>\r\n\t\t\t\t\t\t\t<option value="AK">Alaska</option>\r\n\t\t\t\t\t\t\t<option value="AZ">Arizona</option>\r\n\t\t\t\t\t\t\t<option value="AR">Arkansas</option>\r\n\t\t\t\t\t\t\t<option value="CA">California</option>\r\n\t\t\t\t\t\t\t<option value="CO">Colorado</option>\r\n\t\t\t\t\t\t\t<option value="CT">Connecticut</option>\r\n\t\t\t\t\t\t\t<option value="DE">Delaware</option>\r\n\t\t\t\t\t\t\t<option value="DC">District Of Columbia</option>\r\n\t\t\t\t\t\t\t<option value="FL">Florida</option>\r\n\t\t\t\t\t\t\t<option value="GA">Georgia</option>\r\n\t\t\t\t\t\t\t<option value="HI">Hawaii</option>\r\n\t\t\t\t\t\t\t<option value="ID">Idaho</option>\r\n\t\t\t\t\t\t\t<option value="IL">Illinois</option>\r\n\t\t\t\t\t\t\t<option value="IN">Indiana</option>\r\n\t\t\t\t\t\t\t<option value="IA">Iowa</option>\r\n\t\t\t\t\t\t\t<option value="KS">Kansas</option>\r\n\t\t\t\t\t\t\t<option value="KY">Kentucky</option>\r\n\t\t\t\t\t\t\t<option value="LA">Louisiana</option>\r\n\t\t\t\t\t\t\t<option value="ME">Maine</option>\r\n\t\t\t\t\t\t\t<option value="MD">Maryland</option>\r\n\t\t\t\t\t\t\t<option value="MA">Massachusetts</option>\r\n\t\t\t\t\t\t\t<option value="MI">Michigan</option>\r\n\t\t\t\t\t\t\t<option value="MN">Minnesota</option>\r\n\t\t\t\t\t\t\t<option value="MS">Mississippi</option>\r\n\t\t\t\t\t\t\t<option value="MO">Missouri</option>\r\n\t\t\t\t\t\t\t<option value="MT">Montana</option>\r\n\t\t\t\t\t\t\t<option value="NE">Nebraska</option>\r\n\t\t\t\t\t\t\t<option value="NV">Nevada</option>\r\n\t\t\t\t\t\t\t<option value="NH">New Hampshire</option>\r\n\t\t\t\t\t\t\t<option value="NJ">New Jersey</option>\r\n\t\t\t\t\t\t\t<option value="NM">New Mexico</option>\r\n\t\t\t\t\t\t\t<option value="NY">New York</option>\r\n\t\t\t\t\t\t\t<option value="NC">North Carolina</option>\r\n\t\t\t\t\t\t\t<option value="ND">North Dakota</option>\r\n\t\t\t\t\t\t\t<option value="OH">Ohio</option>\r\n\t\t\t\t\t\t\t<option value="OK">Oklahoma</option>\r\n\t\t\t\t\t\t\t<option value="OR">Oregon</option>\r\n\t\t\t\t\t\t\t<option value="PA">Pennsylvania</option>\r\n\t\t\t\t\t\t\t<option value="RI">Rhode Island</option>\r\n\t\t\t\t\t\t\t<option value="SC">South Carolina</option>\r\n\t\t\t\t\t\t\t<option value="SD">South Dakota</option>\r\n\t\t\t\t\t\t\t<option value="TN">Tennessee</option>\r\n\t\t\t\t\t\t\t<option value="TX">Texas</option>\r\n\t\t\t\t\t\t\t<option value="UT">Utah</option>\r\n\t\t\t\t\t\t\t<option value="VT">Vermont</option>\r\n\t\t\t\t\t\t\t<option value="VA">Virginia</option>\r\n\t\t\t\t\t\t\t<option value="WA">Washington</option>\r\n\t\t\t\t\t\t\t<option value="WV">West Virginia</option>\r\n\t\t\t\t\t\t\t<option value="WI">Wisconsin</option>\r\n\t\t\t\t\t\t\t<option value="WY">Wyoming</option>\r\n\t\t\t\t\t\t</select>\r\n\t\t\t\t\t\t<span class="label-float">State</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="input-container right col-2">\r\n\t\t\t\t\t\t<input type="text" name="zip" id="zip" />\r\n\t\t\t\t\t\t<span class="label-float">Zip Code</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\r\n\t\t\t\t<div class="post-input" data-block="description" data-next="price">\r\n\t\t\t\t\t<label class="question">What do you want people to know about your apartment? Be descriptive.</label>\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<textarea type="text" name="description" id="description"></textarea>\r\n\t\t\t\t\t\t<span class="label-float">Description</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\r\n\t\t\t\t<div class="post-input" data-block="price" data-next="costs">\r\n\t\t\t\t\t<label class="question">What is the price going to be?</label>\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="price" id="price" />\r\n\t\t\t\t\t\t<span class="label-float">Price</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\r\n        <div class="post-input" data-block="costs" data-next="housing">\r\n          <label class="question">Are there other costs such as utilites or a deposit?</label>\r\n          <div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="utilities" id="utilities" class="empty" />\r\n\t\t\t\t\t\t<span class="label-float">Cost of Utilities</span>\r\n\t\t\t\t\t</div>\r\n          <div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="deposit" id="deposit" class="empty" />\r\n\t\t\t\t\t\t<span class="label-float">Cost of Deposit</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="other-costs" id="other-costs" class="empty" />\r\n\t\t\t\t\t\t<span class="label-float">Other Costs</span>\r\n\t\t\t\t\t</div>\r\n        </div>\r\n\r\n\t\t\t\t<div class="post-input" data-block="housing" data-next="numbers">\r\n\t\t\t\t\t<label class="question">What type of housing is this?</label>\r\n\r\n\t\t\t\t\t<div class="input-container radio">\r\n\t\t\t\t\t\t<input type="radio" name="housing-type" id="apartment" />\r\n\t\t\t\t\t\t<label for="apartment">Apartment</label>\r\n\t\t\t\t\t\t<input type="radio" name="housing-type" id="house" />\r\n\t\t\t\t\t\t<label for="house">House/Condo/Duplex</label>\r\n\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t<label class="question">What is the bedroom type?</label>\r\n\r\n\t\t\t\t\t<div class="input-container radio">\r\n\t\t\t\t\t\t<input type="radio" name="bedroom" id="single" />\r\n\t\t\t\t\t\t<label for="single">Single</label>\r\n\t\t\t\t\t\t<input type="radio" name="bedroom" id="married" />\r\n\t\t\t\t\t\t<label for="married">Married</label>\r\n\t\t\t\t\t\t<br><br>\r\n\t\t\t\t\t\t<input type="radio" name="shared" id="private" />\r\n\t\t\t\t\t\t<label for="private">Private, with room mates</label>\r\n\t\t\t\t\t\t<input type="radio" name="shared" id="shared" />\r\n\t\t\t\t\t\t<label for="shared">Shared, with room mates</label>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\r\n\t\t\t\t<div class="post-input" data-block="numbers" data-next="amenities">\r\n\t\t\t\t\t<label class="question">How many bedrooms are there?</label>\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="bedrooms" id="bedrooms" />\r\n\t\t\t\t\t\t<span class="label-float">Number of bedrooms</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<label class="question">How about bathrooms?</label>\r\n\t\t\t\t\t<div class="input-container">\r\n\t\t\t\t\t\t<input type="text" name="bathrooms" id="bathrooms" />\r\n\t\t\t\t\t\t<span class="label-float">Number of bathrooms</span>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\r\n\t\t\t\t<div class="post-input" data-block="amenities" data-next="contracts">\r\n\t\t\t\t\t<label class="question">Check all the cool things your apartment has</label>\r\n')
        for amenity in amenities:
            __M_writer('\t\t\t\t\t\t<input type="checkbox" name="')
            __M_writer(str( amenity.id ))
            __M_writer('" id="')
            __M_writer(str( amenity.amenity ))
            __M_writer('" />\r\n\t\t\t\t\t\t<label for="')
            __M_writer(str( amenity.amenity ))
            __M_writer('">')
            __M_writer(str( amenity.amenity ))
            __M_writer('</label>\r\n')
        __M_writer('        </div>\r\n\r\n        <div class="post-input" data-block="contracts" data-next="leaving">\r\n          <label class="question">How many contracts are available?</label>\r\n          <div class="input-container">\r\n            <input type="text" name="contracts" id="contracts" />\r\n            <span class="label-float">Number of contracts</span>\r\n          </div>\r\n        </div>\r\n\r\n        <div class="post-input" data-block="leaving">\r\n          <label class="question">Why are you leaving your contract?</label>\r\n          <div class="input-container">\r\n            <textarea type="text" name="leaving" id="leaving" /></textarea>\r\n            <span class="label-flaot">Reason for leaving</span>\r\n\r\n  \t\t\t\t\t<input type="submit" value="Post" />\r\n            <input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(str( csrf_token ))
        __M_writer("' />\r\n          </div>\r\n\t\t\t\t</div>\r\n\t\t\t</form>\r\n\t\t</div>\r\n\r\n\t\t<footer>\r\n            Copyright &copy; ")
        __M_writer(str( datetime.now().year ))
        __M_writer(' Candor Contracts\r\n        </footer>\r\n\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post.html", "source_encoding": "utf-8", "line_map": {"128": 267, "129": 267, "130": 267, "131": 267, "132": 269, "133": 286, "134": 286, "135": 293, "136": 293, "142": 136, "16": 2, "29": 0, "45": 1, "46": 2, "51": 87, "56": 297, "61": 301, "67": 299, "73": 299, "79": 4, "88": 4, "89": 6, "90": 16, "91": 16, "92": 18, "93": 19, "94": 20, "95": 21, "96": 23, "97": 49, "98": 63, "99": 67, "100": 68, "101": 69, "102": 70, "103": 71, "104": 71, "105": 82, "111": 89, "119": 89, "120": 92, "121": 92, "122": 265, "123": 266, "124": 266, "125": 266, "126": 266, "127": 266}, "filename": "C:\\Users\\Daniel\\Documents\\Candor\\Candor\\sell\\templates/post.html"}
__M_END_METADATA
"""

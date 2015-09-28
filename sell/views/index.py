from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
import sell.models as smod
from django_mako_plus.controller.router import get_renderer
import os, helpers, json
from helpers import login_required
from django.core.mail import send_mail
# from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

templater = get_renderer('sell')


@view_function
@login_required()
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()

    return templater.render_to_response(request, 'index.html', params)


@view_function
@login_required()
def dashboard(request):
    params = {}
    return templater.render_to_response(request, 'dashboard.html', params)


@view_function
@login_required()
def messages(request):
    params = {}
    return templater.render_to_response(request, 'messages.html', params)


@view_function
@login_required()
def post(request):
    params = {}
    return templater.render_to_response(request, 'post.html', params)


@view_function
@login_required()
def edit(request):
    params = {}
    return templater.render_to_response(request, 'edit.html', params)

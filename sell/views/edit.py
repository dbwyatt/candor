from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import helpers
from helpers import login_required
import json
import os
import requests
import homepage.models as hmod
import sell.models as smod

templater = get_renderer('sell')


@view_function
@login_required()
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()
    params['posts'] = smod.Post.objects.filter(owner_id=hmod.Users.objects.get(id=request.session['user']['id']))

    if request.urlparams[0]:
        post_id, status = request.urlparams[0].split('-')
        post = smod.Post.objects.get(id=post_id)
        post.status = status
        post.save()
        return HttpResponseRedirect('/sell/edit/')

    return templater.render_to_response(request, 'edit.html', params)

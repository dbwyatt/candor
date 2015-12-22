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
from sell.forms import PostForm
import sell.models as smod

templater = get_renderer('sell')


@view_function
@login_required()
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()

    post = smod.Post.objects.filter(id=request.urlparams[0]).first()

    if request.session['user']['id'] != post.owner_id:
        # TODO: Notify the user that they tried to edit a post they didn't own.
        return HttpResponseRedirect('/sell/edit/')

    form = PostForm(request, post)

    # if request.method == 'POST':
        # Update post.

    # If not a POST request, display form.
    params['form'] = form

    return templater.render_to_response(request, 'edit_post.html', params)

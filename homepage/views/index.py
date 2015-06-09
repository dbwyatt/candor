from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import os, helpers

templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()

    return templater.render_to_response(request, 'index.html', params)


@view_function
def register(request):
	first_name = request.urlparams[0]
	last_name = request.urlparams[1]
	email = request.urlparams[2]


class registration_form(forms.Form):
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	
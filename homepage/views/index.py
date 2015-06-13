from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import os, helpers, json

templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()
    params['form'] = registrationForm()

    return templater.render_to_response(request, 'index.html', params)


@view_function
def register(request):
    params = {}

    form = registrationForm()

    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            reg = hmod.emails()
            reg.first_name = form.cleaned_data['first_name']
            reg.last_name = form.cleaned_data['last_name']
            reg.email = form.cleaned_data['email']
            reg.save()
            params = True
            return HttpResponse(params)

    params['form'] = form

    return templater.render_to_response(request, 'early_registration.html', params)


class registrationForm(forms.Form):
	first_name = forms.CharField(label='First Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'type': 'text', 'name': 'firstname', 'id': 'first-name'}))
	last_name = forms.CharField(label='Last Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'type': 'text', 'name': 'lastname', 'id': 'last-name'}))
	email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email', 'name': 'email', 'id': 'email'}))

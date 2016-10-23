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
import requests

templater = get_renderer('buy')


@view_function
@login_required()
def process_request(request):
    params = {}
    params['environment'] = helpers.get_settings_environment()
    
    request.session['active'] = 'buy'

    params['contact'] = contactForm()

    try:
        post = smod.Post.objects.get(id=request.urlparams[0])
        params['post'] = post
        params['pictures'] = post.picture_set.all()
    except:
        HttpResponseRedirect('/buy/')
    
    return templater.render_to_response(request, 'post.html', params)


class contactForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'type': 'text', 'name': 'name', 'id': 'name'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'placeholder': 'Your email', 'type': 'email', 'name': 'email', 'id': 'contact-email'}))
    subject = forms.CharField(label='Subject', required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'type': 'text', 'name': 'subject', 'id': 'subject'}))
    message = forms.CharField(label='Message', required=True, widget=forms.Textarea(attrs={'placeholder': 'Message', 'type': 'text', 'name': 'message', 'id': 'message'}))

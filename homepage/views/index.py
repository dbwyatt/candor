from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import os, helpers, json
from django.core.mail import send_mail
# from django.core.context_processors import csrf

templater = get_renderer('homepage')


@view_function
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()
    params['form'] = registrationForm()
    params['contact'] = contactForm()

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

    return templater.render_to_response(request, 'early_registration_form.html', params)


@view_function
def contact(request):
    params = {}

    form = contactForm()

    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            email = {}

            email['sender'] = form.cleaned_data['name']
            email['sender_email'] = form.cleaned_data['email']
            email['message'] = form.cleaned_data['message']

            emailsubject = form.cleaned_data['subject']
            to_email = 'candorcontracts@gmail.com'
            from_email = form.cleaned_data['email']
            emailbody = templater.render(request, 'contact_email.html', email)
            send_mail(emailsubject, emailbody, from_email, [to_email], html_message=emailbody, fail_silently=False)

            params = True
            return HttpResponse(params)

    params['contact'] = form

    return templater.render_to_response(request, 'contact_form.html', params)


class registrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'type': 'text', 'name': 'firstname', 'id': 'first-name'}))
    last_name = forms.CharField(label='Last Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'type': 'text', 'name': 'lastname', 'id': 'last-name'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email', 'name': 'email', 'id': 'email'}))


class contactForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'type': 'text', 'name': 'name', 'id': 'name'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'placeholder': 'Your email', 'type': 'email', 'name': 'email', 'id': 'contact-email'}))
    subject = forms.CharField(label='Subject', required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'type': 'text', 'name': 'subject', 'id': 'subject'}))
    message = forms.CharField(label='Message', required=True, widget=forms.Textarea(attrs={'placeholder': 'Message', 'type': 'text', 'name': 'message', 'id': 'message'}))

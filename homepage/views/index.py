from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
import sell.models as smod
from django_mako_plus.controller.router import get_renderer
import os, helpers, json
from django.core.mail import send_mail
# from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

templater = get_renderer('homepage')


@view_function
def process_request(request):
    request.session['active'] = 'home'

    params = {}
    params['environment'] = helpers.get_environment()
    params['form'] = registrationForm()
    params['contact'] = contactForm()
    if request.method == 'POST':
        if request.POST.get('set') == 'true':
            user = request.POST
            print(user)
            try:
                users = hmod.Users.objects.get(email=user['email'])
                users.name = user['name']
                users.first_name = user['name'].split()[0]
                users.last_name = user['name'].split()[1]
                users.email = user['email']
                users.image = user['image']
                users.reference_id = user['id_token']
                users.save()
            except hmod.Users.DoesNotExist:
                users = hmod.Users()
                users.name = user['name']
                users.first_name = user['name'].split()[0]
                users.last_name = user['name'].split()[1]
                users.email = user['email']
                users.image = user['image']
                users.reference_id = user['id_token']
                users.save()

            request.session['user'] = {}
            request.session['user']['id'] = users.id
            request.session['user']['name'] = user['name'].split()
            request.session['user']['email'] = user['email']
            request.session['user']['image'] = user['image']
            request.session['user']['last_login'] = {}
            request.session['user']['last_login']['date'] = datetime.now().strftime("%Y-%m-%d")
            request.session['user']['last_login']['time'] = datetime.now().strftime("%I:%M %p")
            request.session['user']['logged_in'] = True
            request.session.modified = True
        else:
            del request.session['user']

        return HttpResponse(True)

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

            if request.META['HTTP_REFERER'].index('/buy/'):
                email['post'] = smod.Post.objects.get(id=request.POST.get('post-id'))
                print(email['post'].title)
                emailbody = templater.render(request, '/buy/templates/buy_email.html', email)
            else:
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


@view_function
def set_user(request):
    user = request.POST
    print(user)
    request.session['user'] = {}
    request.session['user']['name'] = user['name']
    request.session['user']['email'] = user['email']
    request.session['user']['image'] = user['image']
    request.session['user']['loggin_in'] = True

    return HttpResponse(True)

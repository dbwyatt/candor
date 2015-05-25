from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import os

templater = get_renderer('homepage')


@view_function
def process_request(request):
    items = {}
    print('hi')
    print(os.path.dirname(os.path.realpath(__file__)))

    return templater.render_to_response(request, 'index.html', items)

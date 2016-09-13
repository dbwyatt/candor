from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import os
from functools import wraps


def get_environment():
    return os.path.dirname(os.path.dirname(__file__))


def login_required(redirect=None):
    def _login_required(view):
        def _decorator(request, *args, **kwargs):
            if 'user' in request.session:
                return view(request, *args, **kwargs)
            else:
                if redirect is None:
                    return HttpResponseRedirect('/homepage/#login')
                else:
                    return HttpResponseRedirect(redirect)
        return wraps(view)(_decorator)
    return _login_required

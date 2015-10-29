from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import os, helpers, json
from django.contrib.auth.decorators import login_required

templater = get_renderer('accounts')


@view_function
def process_request(request):

    params = {}

    request.session['user']['last_login']['time'] = request.session['user']['last_login']['time'].lstrip("0")
    request.session.modified = True
    return templater.render_to_response(request, 'index.html', params)

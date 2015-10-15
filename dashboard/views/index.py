from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
import dashboard.models as dmod
import sell.models as smod

templater = get_renderer('dashboard')


@view_function
def process_request(request):
    params = {}
    params['recent_search'] = dmod.Search.objects.filter()
    params['messages'] = dmod.Messages.objects.filter(to_user_id=request.session['user']['id'])[:3]
    # params['post'] = smod.Posting.objects.filter()

    return templater.render_to_response(request, 'index.html', params)

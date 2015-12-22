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
    params['environment'] = helpers.get_environment()
    request.session['active'] = 'buy'

    LocationSearch()

    return templater.render_to_response(request, 'index.html', params)


def LocationSearch(address=""):

    address1 = "1600+Amphitheatre+Parkway,+Mountain+View,+CA"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % address1

    response = requests.get(url)
    jsongeocode = response.json()
    # jsonarray = jsongeocode['results'][0]['geometry']
    # print(jsongeocode) #debugging purposes
    # print(jsongeocode['results']) #debugging purposes
    # lnglat = jsonarray['location']
    # lng = lnglat['lng']
    # lat = lnglat['lat']
    lng = jsongeocode['results'][0]['geometry']['location']['lng']
    lat = jsongeocode['results'][0]['geometry']['location']['lat']

    print(lng) #debugging purposes
    print(lat) #debugging purposes

    list1 = smod.Apartment.objects.filter(
        coordinatesLng__range=(lng + 1.0005000, lng - 1.0005000),
        coordinatesLat__range=(lat - 1.0005000, lat + 1.0005000)
    )
    list2 = smod.Apartment.objects.all()
    print(list1)
    print(list2)



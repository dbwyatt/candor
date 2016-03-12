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

    # LocationSearch()

    form = BuyForm()

    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            posts = smod.Post.objects.all()
            return HttpResponse()

    params['form'] = form

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
        longitude__range=(lng + 1.0005000, lng - 1.0005000),
        latitude__range=(lat - 1.0005000, lat + 1.0005000)
    )
    list2 = smod.Apartment.objects.all()
    print(list1)
    print(list2)


@view_function
@login_required()
def search(request):
    params = {}
    form = BuyForm()

    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            for x, i in form.cleaned_data.items():
                print(x, i)
            results = smod.Post.objects.all()
            params = True
            return HttpResponse(results)

    params['form'] = form

    return templater.render_to_response(request, 'search_form.html', params)


class BuyForm(forms.Form):
    min_price = forms.CharField(label='Min Price', required=False, widget=forms.NumberInput(attrs={'type': 'number', 'name': 'min-price', 'id': 'min-price'}))
    max_price = forms.CharField(label='Max Price', required=False, widget=forms.NumberInput(attrs={'type': 'number', 'name': 'max-price', 'id': 'max-price'}))
    location = forms.CharField(label='City, State', required=False, widget=forms.TextInput(attrs={'type': 'text', 'name': 'location', 'id': 'location', 'class': 'controls', 'placeholder': ''}))
    bath_number = forms.ChoiceField(label='Bathrooms', required=False, widget=forms.Select(attrs={'type': 'number', 'name': 'bath-number', 'id': 'bath-number'}), choices=[(x,'{}+ Bathrooms'.format(x)) for x in range(5) if x != 0])
    bed_number = forms.ChoiceField(label='Bedrooms', required=False, widget=forms.Select(attrs={'type': 'number', 'name': 'bed-number', 'id': 'bed-number'}), choices=[(x,'{}+ Bedrooms'.format(x)) for x in range(5) if x != 0])
    amenities = forms.MultipleChoiceField(label='Amenities', required=False, widget=forms.SelectMultiple(attrs={'type': 'text', 'name': 'amenities', 'id': 'amenities'}), choices=[[amenity.id, amenity.amenity] for amenity in smod.Amenity.objects.all().order_by('amenity')])
    gender = forms.ChoiceField(label='Type', required=False, widget=forms.Select(attrs={'type': 'text', 'name': 'gender', 'id': 'gender'}), choices=[(0,'Male'),(1, 'Female')])
    friend_email = forms.EmailField(label='Friend Email', required=False, widget=forms.EmailInput(attrs={'type': 'email', 'name': 'friend-email', 'id': 'friend-email'}))

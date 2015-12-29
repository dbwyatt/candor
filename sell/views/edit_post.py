from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import helpers
from helpers import login_required
import json
import os
import requests
import homepage.models as hmod
from sell.forms import PostForm
from sell.helpers import save_and_return_uploaded_image
import sell.models as smod

templater = get_renderer('sell')


@view_function
@login_required()
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()
    form = PostForm(request)

    post = smod.Post.objects.get(id=request.urlparams[0])

    if request.session['user']['id'] != post.owner_id:
        # TODO: Notify the user that they tried to edit a post they didn't own.
        return HttpResponseRedirect('/sell/edit/')

    if request.method == 'POST':
        form = PostForm(request, request.POST)
        if form.is_valid():
            print("form is valid")
            full_address = form.cleaned_data['address1'] + ' ' + form.cleaned_data['address2'] + ', ' + form.cleaned_data['city'] + ', ' + form.cleaned_data['state'] + ' ' + str(form.cleaned_data['zip'])
            search_address = form.cleaned_data['address1'] + ', ' + form.cleaned_data['city'] + ', ' + form.cleaned_data['state'] + ' ' + str(form.cleaned_data['zip']).replace(' ', '+')
            geo_address = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + search_address)
            parsed_geo = geo_address.json()

            apartment = post.apartment
            apartment.complex = form.cleaned_data['complex']
            apartment.full_address = full_address
            apartment.address1 = form.cleaned_data['address1']
            apartment.address2 = form.cleaned_data['address2']
            apartment.city = form.cleaned_data['city']
            apartment.state = form.cleaned_data['state']
            apartment.zip = form.cleaned_data['zip']
            apartment.latitude = parsed_geo['results'][0]['geometry']['location']['lat'] if len(parsed_geo['results']) > 0 else 0
            apartment.longtitude = parsed_geo['results'][0]['geometry']['location']['lng'] if len(parsed_geo['results']) > 0 else 0
            apartment.housing_type = form.cleaned_data['housing_type']
            apartment.single_or_married = form.cleaned_data['single_or_married']
            apartment.male_or_female = form.cleaned_data['male_or_female']
            apartment.bed_number = form.cleaned_data['bed_number']
            apartment.bed_type = form.cleaned_data['bed_type']
            apartment.bath_number = form.cleaned_data['bath_number']
            apartment.utilities = form.cleaned_data['utilities'] if form.cleaned_data['utilities'] else 0
            apartment.save()

            post.title = form.cleaned_data['title']
            post.description = form.cleaned_data['description']
            post.price = form.cleaned_data['price']
            post.deposit = form.cleaned_data['deposit'] if form.cleaned_data['deposit'] else 0
            post.bounty = form.cleaned_data['bounty'] if form.cleaned_data['bounty'] else 0
            post.contracts = form.cleaned_data['contracts']
            post.availability = form.cleaned_data['availability']
            post.leaving = form.cleaned_data['leaving']
            post.save()

            # TODO: Add Facebook link.

            if request.FILES.get('image'):
                picture = smod.Picture.objects.create(
                    post=post,
                    picture=save_and_return_uploaded_image(request.FILES['image'], request.session['user']['id']),
                )
            if request.FILES.get('image2'):
                picture = smod.Picture.objects.create(
                    post=post,
                    picture=save_and_return_uploaded_image(request.FILES['image2'], request.session['user']['id']),
                )
            if request.FILES.get('image3'):
                picture = smod.Picture.objects.create(
                    post=post,
                    picture=save_and_return_uploaded_image(request.FILES['image3'], request.session['user']['id']),
                )

            # TODO: Implement videos.

            apartment.amenity.clear()
            if form.cleaned_data['amenities']:
                for amen in form.cleaned_data['amenities']:
                    apartment.amenity.add(smod.Amenity.objects.filter(id=amen).first())

            return HttpResponseRedirect('/sell/edit/')

    # If not a POST request, display form.
    form = PostForm(request, initial={
        'title': post.title,
        'complex': post.apartment.complex,
        'address1': post.apartment.address1,
        'address2': post.apartment.address2,
        'city': post.apartment.city,
        'state': post.apartment.state,
        'zip': post.apartment.zip,
        'description': post.description,
        'price': post.price,
        'utilities': post.apartment.utilities,
        'deposit': post.deposit,
        'bounty': post.bounty,
        'housing_type': post.apartment.housing_type,
        'single_or_married': post.apartment.single_or_married,
        'male_or_female': post.apartment.male_or_female,
        'bed_type': post.apartment.bed_type,
        'bed_number': post.apartment.bed_number,
        'bath_number': post.apartment.bath_number,
        'amenity': post.apartment.amenity,
        'contracts': post.contracts,
        'leaving': post.leaving,
        'availability': post.availability
        # TODO: Add images.
    })

    params['form'] = form

    return templater.render_to_response(request, 'edit_post.html', params)

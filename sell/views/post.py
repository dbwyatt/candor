from django import forms
from django.conf import settings
from django.core.mail import send_mail
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
    request.session['active'] = 'post'
    if 'user' not in request.session:
        request.session['user'] = {}
    request.session['user']['menu_status'] = 'open'
    request.session.modified = True

    form = PostForm(request, initial={'state': 'UT'})

    if request.method == 'POST':
        files = request.FILES.getlist('myfiles')
        # del request.FILES
        form = PostForm(request, request.POST)

        if form.is_valid():
            full_address = form.cleaned_data['address1'] + ' ' + form.cleaned_data['address2'] + ', ' + form.cleaned_data['city'] + ', ' + form.cleaned_data['state'] + ' ' + str(form.cleaned_data['zip'])
            search_address = form.cleaned_data['address1'] + ', ' + form.cleaned_data['city'] + ', ' + form.cleaned_data['state'] + ' ' + str(form.cleaned_data['zip']).replace(' ', '+')
            geo_address = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + search_address)
            parsed_geo = geo_address.json()

            apartment = smod.Apartment.objects.create(
                complex=form.cleaned_data['complex'],
                full_address=full_address,
                address1=form.cleaned_data['address1'],
                address2=form.cleaned_data['address2'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zip=form.cleaned_data['zip'],
                latitude=parsed_geo['results'][0]['geometry']['location']['lat'] if len(parsed_geo['results']) > 0 else 0,
                longitude=parsed_geo['results'][0]['geometry']['location']['lng'] if len(parsed_geo['results']) > 0 else 0,
                housing_type=form.cleaned_data['housing_type'],
                single_or_married=form.cleaned_data['single_or_married'],
                male_or_female=form.cleaned_data['male_or_female'],
                bed_number=form.cleaned_data['bed_number'],
                bed_type=form.cleaned_data['bed_type'],
                bath_number=form.cleaned_data['bath_number'],
                utilities=form.cleaned_data['utilities'] if form.cleaned_data['utilities'] else 0
            )

            post = smod.Post.objects.create(
                owner=hmod.Users.objects.filter(id=request.session['user']['id']).first(),
                apartment=apartment,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                deposit=form.cleaned_data['deposit'] if form.cleaned_data['deposit'] else 0,
                bounty=form.cleaned_data['bounty'] if form.cleaned_data['bounty'] else 0,
                # contracts=form.cleaned_data['contracts'],
                availability=form.cleaned_data['availability'],
                leaving=form.cleaned_data['leaving'],
                status='active',
                roommate_number=form.cleaned_data['roommate_number']
            )

            # TODO: Add Facebook link.

            for a_file in files:
                print('line 83')
                print(a_file.name)
                smod.Picture.objects.create(
                    post=post,
                    file_name=a_file.name,
                    attachment=a_file
                )

            # if request.FILES.get('image'):
            #     picture = smod.Picture.objects.create(
            #         post=post,
            #         picture=save_and_return_uploaded_image(request.FILES['image'], request.session['user']['id']),
            #     )
            # if request.FILES.get('image2'):
            #     picture = smod.Picture.objects.create(
            #         post=post,
            #         picture=save_and_return_uploaded_image(request.FILES['image2'], request.session['user']['id']),
            #     )
            # if request.FILES.get('image3'):
            #     picture = smod.Picture.objects.create(
            #         post=post,
            #         picture=save_and_return_uploaded_image(request.FILES['image3'], request.session['user']['id']),
            #     )

            # TODO: Implement videos.

            if form.cleaned_data['amenities']:
                for amen in form.cleaned_data['amenities']:
                    apartment.amenity.add(smod.Amenity.objects.filter(id=amen).first())

            # Redirect to dashboard. TODO: Need to provide confirmation.
            return HttpResponseRedirect('/sell/post/?success')

        else:
            print(form.errors)

    params['form'] = form

    return templater.render_to_response(request, 'post.html', params)

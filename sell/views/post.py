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
from datetime import datetime

templater = get_renderer('sell')


@view_function
@login_required()
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()
    params['amenities'] = smod.Amenity.objects.all()

    # TODO: Use validated data instead of using the data from request.POST.
    # https://docs.djangoproject.com/en/1.7/topics/forms/#field-data

    if request.method == 'POST':
        p = request.POST

        avail_date = [int(num) for num in p['availability'].split('-')]

        apartment = smod.Apartment.objects.create(
            complex=p['complex'],
            address=[p['address1'], p['address2'], p['city'], p['state'], p['zip']],
            housing_type=p.get('housing-type', 'Apartment'),
            single_or_married=p.get('single-or-married', 'Single'),
            bed_number=p['bed-number'],
            bed_type=p.get('bed-type', 'Private'),
            bath_number=float(p['bath-number']),
            utilities=float(p['utilities']) if p['utilities'] else 0
        )

        post = smod.Post.objects.create(
            owner=hmod.Users.objects.filter(id=request.session['user']['id']).first(),
            apartment=apartment,
            title=p['title'],
            description=p['description'],
            price=float(p['price']),
            deposit=float(p['deposit']) if p['deposit'] else 0,
            bounty=float(p['bounty']) if p['bounty'] else 0,
            contracts=int(p['contracts']),
            availability=datetime(avail_date[0], avail_date[1], avail_date[2]),
            leaving=p['leaving']
            # video=None,
            # pictures=None,
        )

        # Add Amenities to post.
        for key in p:
            if key.split()[0] == 'Amenity':
                post.amenity.add(smod.Amenity.objects.filter(id=key.split()[1]).first())

        # Redirect to dashboard. Provide confirmation.

    return templater.render_to_response(request, 'post.html', params)

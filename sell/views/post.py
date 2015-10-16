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
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

templater = get_renderer('sell')


@view_function
@login_required()
def process_request(request):
    if request.method == 'POST':
        p = request.POST

        for key, value in p.items():
            print("{0}: {1}".format(key, value))

        apartment = smod.Apartment.objects.create(
            year=int(p['year']),
            address=[p['address1'], p['address2'], p['city'], p['state'], p['zip']],
            bed_number=1,
            number_of_shared_bed=1,
            number_of_single_bed=1,
            bath_number=float(p['bathrooms']),
            utilities=float(p['utilities'])
        )

        smod.Post.objects.create(
            owner=hmod.User.objects.filter(email=request.session['user']['email']).first(),  # This looks to be working.
            apartment=apartment,
            title=p['title'],
            description=p['description'],
            bedroom='Shared',
            price=float(p['price']),
            deposit=float(100),
            bounty=float(100),
            availability=datetime.date,
            video=None,
            pictures=None,
            amenity=None
        )
        print(smod.Posting.objects.all())
        # Redirect to dashboard. Provide confirmation.
    else:
        params = {}
        params['environment'] = helpers.get_environment()
        params['amenities'] = smod.Amenity.objects.all()

        return templater.render_to_response(request, 'post.html', params)

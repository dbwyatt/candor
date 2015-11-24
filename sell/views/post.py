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
import sell.models as smod

templater = get_renderer('sell')


@view_function
@login_required()
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()
    params['form'] = PostForm(request)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            avail_date = [int(num) for num in form.cleaned_data['availability'].split('-')]

            full_address = form.cleaned_data['address1'] + ' ' + form.cleaned_data['address2'] + ', ' + form.cleaned_data['city'] + ', ' + form.cleaned_data['state'] + form.cleaned_data['zip']
            search_address = full_address.replace(' ', '+')
            geo_address = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + search_address).text
            parsed_geo = json.loads(geo_address)

            apartment = smod.Apartment.objects.create(
                complex=form.cleaned_data['complex'],
                address=full_address,
                latitude=parsed_geo['results'][0]['geometry']['location']['lat'],
                longtitude=parsed_geo['results'][0]['geometry']['location']['lng'],
                housing_type=form.cleaned_data.get('housing-type', 'Apartment'),
                single_or_married=form.cleaned_data.get('single-or-married', 'Single'),
                bed_number=form.cleaned_data['bed-number'],
                bed_type=form.cleaned_data.get('bed-type', 'Private'),
                bath_number=float(form.cleaned_data['bath-number']),
                utilities=float(form.cleaned_data['utilities']) if form.cleaned_data['utilities'] else 0
            )

            post = smod.Post.objects.create(
                owner=hmod.Users.objects.filter(id=request.session['user']['id']).first(),
                apartment=apartment,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=float(form.cleaned_data['price']),
                deposit=float(form.cleaned_data['deposit']) if form.cleaned_data['deposit'] else 0,
                bounty=float(form.cleaned_data['bounty']) if form.cleaned_data['bounty'] else 0,
                contracts=int(form.cleaned_data['contracts']),
                availability=datetime(avail_date[0], avail_date[1], avail_date[2]),
                leaving=form.cleaned_data['leaving'],
                video=None,  # Implement
                pictures=None  # Implement
            )

            # Add Amenities to post. TODO: Update this to work with form.cleaned_data.
            for key in p:
                if key.split()[0] == 'Amenity':
                    post.amenity.add(smod.Amenity.objects.filter(id=key.split()[1]).first())

            # Redirect to dashboard. TODO: Need to provide confirmation.
            return HttpResponseRedirect('/dashboard/')

    return templater.render_to_response(request, 'post.html', params)


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'name': 'title', 'id': 'title'}))
    complex = forms.CharField(widget=forms.TextInput(attrs={'name': 'complex', 'id': 'complex'}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'name': 'address1', 'id': 'address1'}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'name': 'address2', 'id': 'address2'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'name': 'city', 'id': 'city'}))
    zip = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'zip', 'id': 'zip'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'name': 'description', 'id': 'description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'price', 'id': 'price'}))
    utilities = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'name': 'utilities', 'id': 'utilities'}))
    deposit = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'name': 'deposit', 'id': 'deposit'}))
    bounty = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'name': 'bounty', 'id': 'bounty'}))
    housing_type = forms.ChoiceField(required=False, choices=(('apartment', 'Apartment'), ('house', 'House/Condo/Duplex')), widget=forms.RadioSelect(attrs={'name': 'housing-type', 'id': 'housing-type'}))
    single_or_married = forms.ChoiceField(required=False, choices=(('single', 'Single'), ('married', 'Married')), widget=forms.RadioSelect(attrs={'name': 'single-or-married', 'id': 'single-or-married'}))
    bed_type = forms.ChoiceField(required=False, choices=(('private', 'Private'), ('shared', 'Shared')), widget=forms.RadioSelect(attrs={'name': 'bed-type', 'id': 'bed-type'}))
    bed_number = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'bed-number', 'id': 'bed-number'}))
    bath_number = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'bath-number', 'id': 'bath-number'}))
    contracts = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'contracts', 'id': 'contracts'}))
    availability = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'name': 'availability', 'id': 'availability'}))
    leaving = forms.CharField(widget=forms.Textarea(attrs={'name': 'leaving', 'id': 'leaving'}))

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        self.init()

    def init(self):
        self.fields['state'] = forms.ChoiceField(choices=(('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
         ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'),
         ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
         ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
         ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
         ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
         ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'),
         ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
         ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')), widget=forms.Select(attrs={'name': 'state', 'id': 'state'}))

        self.fields['amenities'] = forms.ChoiceField(required=False, choices=[[amenity.id, amenity.amenity] for amenity in smod.Amenity.objects.all()], widget=forms.CheckboxSelectMultiple(attrs={'name': 'amenity', 'id': 'amenity'}))

    def clean_title(self):
        if len(self.cleaned_data['title']) < 3:
            raise forms.ValidationError("Title needs to be at least 3 characters long.")
        return self.cleaned_data['title']

    def clean_zip(self):
        if len(self.cleaned_data['zip']) != 5:
            raise forms.ValidationError("Please enter a 5 digit zip code.")
        return self.cleaned_data['zip']

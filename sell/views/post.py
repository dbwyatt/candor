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
    form = PostForm(request)

    if request.method == 'POST':
        form = PostForm(request, request.POST)
        if form.is_valid():
            full_address = form.cleaned_data['address1'] + ' ' + form.cleaned_data['address2'] + ', ' + form.cleaned_data['city'] + ', ' + form.cleaned_data['state'] + ' ' + str(form.cleaned_data['zip'])
            search_address = form.cleaned_data['address1'] + ', ' + form.cleaned_data['city'] + ', ' + form.cleaned_data['state'] + ' ' + str(form.cleaned_data['zip']).replace(' ', '+')
            geo_address = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + search_address)
            parsed_geo = geo_address.json()

            apartment = smod.Apartment.objects.create(
                complex=form.cleaned_data['complex'],
                address=full_address,
                latitude=parsed_geo['results'][0]['geometry']['location']['lat'] if len(parsed_geo['results']) > 0 else 0,
                longtitude=parsed_geo['results'][0]['geometry']['location']['lng'] if len(parsed_geo['results']) > 0 else 0,
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
                contracts=form.cleaned_data['contracts'],
                availability=form.cleaned_data['availability'],
                leaving=form.cleaned_data['leaving'],
            )

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

            if form.cleaned_data['amenities']:
                for amen in form.cleaned_data['amenities']:
                    post.amenity.add(smod.Amenity.objects.filter(id=amen).first())

            # Redirect to dashboard. TODO: Need to provide confirmation.
            return HttpResponseRedirect('/dashboard/')

    params['form'] = form

    return templater.render_to_response(request, 'post.html', params)


# FIXME: Not sure this is the right place for this method.
def save_and_return_uploaded_image(img, user_id):
    file_name = datetime.now().strftime('%Y-%m-%d-%H-%M-%S_') + str(user_id) + '_' + str(img)
    with open('post_images/' + file_name, 'wb+') as destination:
        for chunk in img.chunks():
            destination.write(chunk)
    return file_name


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'name': 'title', 'id': 'title'}))
    complex = forms.CharField(widget=forms.TextInput(attrs={'name': 'complex', 'id': 'complex'}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'name': 'address1', 'id': 'address1'}))
    address2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'name': 'address2', 'id': 'address2', 'class': 'empty'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'name': 'city', 'id': 'city'}))
    zip = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'zip', 'id': 'zip'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'name': 'description', 'id': 'description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'price', 'id': 'price'}))
    utilities = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'name': 'utilities', 'id': 'utilities', 'class': 'empty'}))
    deposit = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'name': 'deposit', 'id': 'deposit', 'class': 'empty'}))
    bounty = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'name': 'bounty', 'id': 'bounty', 'class': 'empty'}))
    housing_type = forms.ChoiceField(choices=(('apartment', 'Apartment'), ('house', 'House/Condo/Duplex')), widget=forms.RadioSelect(attrs={'name': 'housing-type', 'id': 'housing-type'}))
    single_or_married = forms.ChoiceField(choices=(('single', 'Single'), ('married', 'Married')), widget=forms.RadioSelect(attrs={'name': 'single-or-married', 'id': 'single-or-married'}))
    male_or_female = forms.ChoiceField(choices=(('male', 'Male'), ('female', 'Female')), widget=forms.RadioSelect(attrs={'name': 'male-or-female', 'id': 'male-or-female'}))
    bed_type = forms.ChoiceField(choices=(('private', 'Private'), ('shared', 'Shared')), widget=forms.RadioSelect(attrs={'name': 'bed-type', 'id': 'bed-type'}))
    bed_number = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'bed-number', 'id': 'bed-number'}))
    bath_number = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'bath-number', 'id': 'bath-number'}))
    contracts = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'contracts', 'id': 'contracts'}))
    leaving = forms.CharField(widget=forms.Textarea(attrs={'name': 'leaving', 'id': 'leaving'}))
    availability = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'name': 'availability', 'id': 'availability'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'name': 'image', 'id': 'image', 'class': 'empty'}))
    image2 = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'name': 'image2', 'id': 'image2', 'class': 'empty'}))
    image3 = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'name': 'image3', 'id': 'image3', 'class': 'empty'}))

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

        self.fields['amenities'] = forms.MultipleChoiceField(required=False, choices=[(amenity.id, amenity.amenity) for amenity in smod.Amenity.objects.all()], widget=forms.CheckboxSelectMultiple(attrs={'name': 'amenity', 'id': 'amenity'}))

    def clean_title(self):
        if len(self.cleaned_data['title']) < 3:
            raise forms.ValidationError("Title needs to be at least 3 characters long.")
        return self.cleaned_data['title']

    def clean_zip(self):
        if len(str(self.cleaned_data['zip'])) != 5:
            raise forms.ValidationError("Please enter a 5 digit zip code.")
        return self.cleaned_data['zip']

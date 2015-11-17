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
    params['form'] = PostForm(request)

    # TODO: Use validated data instead of using the data from request.POST.
    # https://docs.djangoproject.com/en/1.7/topics/forms/#field-data

    if request.method == 'POST':
        #########################################################
        # example for saving form data 
        form = PostForm(request.POST)
        if form.is_valid():
            reg = hmod.emails()
            reg.first_name = form.cleaned_data['first_name']
            reg.last_name = form.cleaned_data['last_name']
            reg.email = form.cleaned_data['email']
            reg.save()

            # in our case
            apartment = smod.Apartment.objects.create(
                complex = form.cleaned_data['complex'],
                address = [form.cleaned_data['address1'], form.cleaned_data['address2'], etc....],
                etc.,
            )
        #########################################################

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

            # Redirect to dashboard. Need to provide confirmation.
            return HttpResponseRedirect('/dashboard/')

    return templater.render_to_response(request, 'post.html', params)

class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'name': 'title', 'id': 'title'}))
    complex = forms.CharField(widget=forms.TextInput(attrs={'name': 'complex', 'id': 'complex'}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'name': 'address1', 'id': 'address1'}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'name': 'address2', 'id': 'address2'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'name': 'city', 'id': 'city'}))
    # state = forms.ChoiceField(choices=self.STATES, widget=forms.Select(attrs={'name': 'state', 'id': 'state'}))
    zip = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'zip', 'id': 'zip'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'name': 'description', 'id': 'description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'price', 'id': 'price'}))
    utilities = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'utilities', 'id': 'utilities'}))
    deposit = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'deposit', 'id': 'deposit'}))
    bounty = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'bounty', 'id': 'bounty'}))
    housing_type = forms.ChoiceField(choices=(('apartment', 'Apartment'), ('house', 'House/Condo/Duplex')), widget=forms.RadioSelect(attrs={'name': 'housing-type', 'id': 'housing-type'}))
    single_or_married = forms.ChoiceField(choices=(('single', 'Single'), ('married', 'Married')), widget=forms.RadioSelect(attrs={'name': 'single-or-married', 'id': 'single-or-married'}))
    bed_type = forms.ChoiceField(choices=(('private', 'Private'), ('shared', 'Shared')), widget=forms.RadioSelect(attrs={'name': 'bed-type', 'id': 'bed-type'}))
    bed_number = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'bed-number', 'id': 'bed-number'}))
    bath_number = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'bath-number', 'id': 'bath-number'}))
    # amenities = forms.ChoiceField(choices=self.amenity_choices, widget=forms.CheckboxSelectMultiple(attrs={'name': 'amenity', 'id': 'amenity'}))
    contracts = forms.DecimalField(widget=forms.NumberInput(attrs={'name': 'contracts', 'id': 'contracts'}))
    availability = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'name': 'availability', 'id': 'availability'}))
    leaving = forms.CharField(widget=forms.Textarea(attrs={'name': 'leaving', 'id': 'leaving'}))

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        self.init()

    def init(self):
        self.fields['state'] = forms.ChoiceField(choices = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
         ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'),
         ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
         ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
         ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
         ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
         ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'),
         ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
         ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')), widget=forms.Select(attrs={'name': 'state', 'id': 'state'}))

        self.fields['amenities'] = forms.ChoiceField(choices=[[amenity.id, amenity.amenity] for amenity in smod.Amenity.objects.all()], widget=forms.CheckboxSelectMultiple(attrs={'name': 'amenity', 'id': 'amenity'}))

        # amenities = smod.Amenity.objects.all()
        # amenity_choices = []
        # for amenity in amenities:
        #     amenity_choices.append(('Amenity ' + str(amenity.id), amenity.amenity))
        # self.amenity_choices = tuple(amenity_choices)

    def clean_title(self):
    if len(self.cleaned_data['title']) < 3:
        raise forms.ValidationError("Title needs to be at least 3 characters long.")
    return self.cleaned_data['title']
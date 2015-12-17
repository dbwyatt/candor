from django import forms
import sell.models as smod

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

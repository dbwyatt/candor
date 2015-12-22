from django.db import models
from homepage import models as hmod


class Post(models.Model):
    owner = models.ForeignKey(hmod.Users)
    apartment = models.ForeignKey('Apartment', default=0)
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=8)
    deposit = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=6)
    bounty = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=6)
    contracts = models.IntegerField(blank=False, null=False)
    availability = models.DateField(blank=False, null=False)
    leaving = models.TextField(blank=False, null=False)
    amenity = models.ManyToManyField('Amenity', blank=True, null=True)


class Amenity(models.Model):
    amenity = models.TextField(blank=False, null=False)


class Picture(models.Model):
    post = models.ForeignKey(Post)
    picture = models.TextField(blank=False, null=False)


class Video(models.Model):
    post = models.ForeignKey(Post)
    video = models.TextField(blank=False, null=False)


class Apartment(models.Model):
    complex = models.TextField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    latitude = models.DecimalField(blank=False, null=False, decimal_places=8, max_digits=12)
    longtitude = models.DecimalField(blank=False, null=False, decimal_places=8, max_digits=12)
    housing_type = models.TextField(blank=False, null=False, default='Apartment')
    single_or_married = models.TextField(blank=False, null=False, default='Single')
    male_or_female = models.TextField(blank=False, null=False)
    bed_number = models.IntegerField(blank=False, null=False)
    bed_type = models.TextField(blank=False, null=False, default='Private')
    bath_number = models.DecimalField(blank=False, null=False, decimal_places=1, max_digits=3)
    utilities = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=6)

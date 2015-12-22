from django.db import models
from homepage import models as hmod

# Define models here


class Post(models.Model):
    owner = models.ForeignKey(hmod.Users)
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    bedroom = models.TextField(blank=False, null=False, default='Single')
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=8)
    deposit = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=6)
    bounty = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)
    amenity = models.ManyToManyField('Amenity')
    availability = models.DateField()
    video = models.TextField(blank=True, null=True)
    pictures = models.ManyToManyField('Picture')


class Amenity(models.Model):
    amenity = models.TextField(blank=False, null=False)


class Picture(models.Model):
    picture = models.TextField(blank=False, null=False)


class Apartment(models.Model):
    year = models.IntegerField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    bed_number = models.IntegerField(blank=False, null=False)
    number_of_shared_bed = models.IntegerField(blank=False, null=False, default=1)
    number_of_single_bed = models.IntegerField(blank=False, null=False, default=1)
    bath_number = models.DecimalField(blank=False, null=False, decimal_places=1, max_digits=3)
    utilities = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=6)
    coordinatesLng = models.DecimalField(blank=False, null=False, decimal_places=7, max_digits=10, default=0)
    coordinatesLat = models.DecimalField(blank=False, null=False, decimal_places=7, max_digits=10, default=0)


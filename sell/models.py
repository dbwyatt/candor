from django.db import models

# Define models here


class Posting(models.Model):
    owner = models.IntegerField(blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    bed_number = models.IntegerField(blank=False, null=False)
    bath_number = models.IntegerField(blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=8)
    amenitiy = models.ManyToManyField('Amenity')


class Amenity(models.Model):
    amenitiy = models.TextField(blank=False, null=False)

from django.db import models

# Define models here


class Posting(models.Model):
    owner = models.IntegerField(blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    bedroom = models.TextField(blank=False, null=False, default='Single')
    bed_number = models.IntegerField(blank=False, null=False)
    number_of_shared_bed = models.IntegerField(blank=False, null=False, default=1)
    number_of_single_bed = models.IntegerField(blank=False, null=False, default=1)
    bath_number = models.DecimalField(blank=False, null=False, decimal_places=1, max_digits=3)
    year = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=8)
    amenitiy = models.ManyToManyField('Amenity')
    availability = models.ManyToManyField('Availability')


class Amenity(models.Model):
    amenity = models.TextField(blank=False, null=False)


class Availability(models.Model):
    availability = models.TextField(blank=False, null=False)

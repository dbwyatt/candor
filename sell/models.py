from django.db import models
from homepage import models as hmod
import os


class Post(models.Model):
    apartment = models.ForeignKey('Apartment', default=0)
    availability = models.DateField(blank=False, null=False)
    bounty = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=6)
    # contracts = models.IntegerField(blank=False, null=False)
    deposit = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=6)
    description = models.TextField(blank=False, null=False)
    facebook_link = models.TextField(blank=True, null=True)
    leaving = models.TextField(blank=False, null=False)
    owner = models.ForeignKey(hmod.Users)
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=8)
    status = models.TextField(blank=False, null=False)  # Options: active, inactive, sold
    title = models.TextField(blank=False, null=False)
    roommate_number = models.IntegerField(blank=False, null=False)


class Apartment(models.Model):
    amenity = models.ManyToManyField('Amenity', blank=True)
    complex = models.TextField(blank=False, null=False)
    full_address = models.TextField(blank=False, null=False)
    address1 = models.TextField(blank=False, null=False)
    address2 = models.TextField(blank=False, null=False)
    city = models.TextField(blank=False, null=False)
    state = models.TextField(blank=False, null=False)
    zip = models.IntegerField(blank=False, null=False)
    latitude = models.DecimalField(blank=False, null=False, decimal_places=8, max_digits=12)
    longitude = models.DecimalField(blank=False, null=False, decimal_places=8, max_digits=12)
    housing_type = models.TextField(blank=False, null=False)
    single_or_married = models.TextField(blank=False, null=False)
    male_or_female = models.TextField(blank=False, null=False)
    bed_number = models.IntegerField(blank=False, null=False)
    bed_type = models.TextField(blank=False, null=False)
    bath_number = models.DecimalField(blank=False, null=False, decimal_places=1, max_digits=3)
    utilities = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=6)


class School(models.Model):
    school = models.TextField(blank=False, null=False)


class Amenity(models.Model):
    amenity = models.TextField(blank=False, null=False)

def content_file_name(instance, filename):
    return os.path.join(*["sell/media/post_images", filename])

class Picture(models.Model):
    post = models.ForeignKey(Post)
    file_name = models.CharField(blank=False, null=False, max_length=100)
    attachment = models.FileField(upload_to=content_file_name)

class Video(models.Model):
    post = models.ForeignKey(Post)
    video = models.TextField(blank=False, null=False)

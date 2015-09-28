from django.db import models


# Define models here
class emails(models.Model):

    """
    Description: Stores email information for
    those that want to be notified when Candor is ready
    """
    first_name = models.TextField(blank=False, null=False)
    last_name = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, max_length=100)


class Users(models.Model):

    """
    Description: This currently is to handle users
    logged in with only Google or Facebook to handle
    their associated information. Normal Django User
    class will be instantiated shortly
    """
    name = models.TextField(blank=False, null=False)
    first_name = models.TextField(blank=False, null=False)
    last_name = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    image = models.TextField(blank=False, null=False)
    reference_id = models.TextField(blank=False, null=False)

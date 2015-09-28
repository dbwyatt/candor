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

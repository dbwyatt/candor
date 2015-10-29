from django.db import models
from homepage import models as hmod


# Define models here
class Search(models.Model):
    user = models.ForeignKey(hmod.Users)
    search = models.TextField()


class Messages(models.Model):
    from_user = models.ForeignKey(hmod.Users, related_name="from_user")
    to_user = models.ForeignKey(hmod.Users, related_name="to_user")
    time_sent = models.DateTimeField()
    message = models.TextField()
    read = models.BooleanField(default=None)

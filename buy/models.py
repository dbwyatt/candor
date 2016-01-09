from django.db import models
from django.utils import timezone
from homepage import models as hmod
from datetime import datetime
import requests

# Define models here


class SearchEntry(models.Model):
    url = models.TextField(blank=False, null=False)
    user = models.ForeignKey(hmod.Users)
    date = models.DateTimeField(blank=False, null=False, default=timezone.now)

    def table_sizer(self, user):
        max_size = 100
        current_searches = SearchEntry.objects.filter(user=user).order_by('date')
        size = len(current_searches)

        if size > max_size:
            # delete everything after number 100
            history_slice = current_searches[0:99]
            SearchEntry.objects.filter(user=user).order_by('date')[100].delete()

        return history_slice

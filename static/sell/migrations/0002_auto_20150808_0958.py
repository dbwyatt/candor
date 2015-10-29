# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amenity',
            old_name='amenitiy',
            new_name='amenity',
        ),
        migrations.AddField(
            model_name='posting',
            name='bedroom',
            field=models.TextField(default='Single'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posting',
            name='number_of_shared_bed',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posting',
            name='number_of_single_bed',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='posting',
            name='bath_number',
            field=models.DecimalField(max_digits=3, decimal_places=1),
            preserve_default=True,
        ),
    ]

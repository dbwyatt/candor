# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('amenitiy', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('title', models.TextField()),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('bed_number', models.IntegerField()),
                ('bath_number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amenitiy', models.ManyToManyField(to='sell.Amenity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
        ('sell', '0003_auto_20151002_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('address', models.TextField()),
                ('bed_number', models.IntegerField()),
                ('number_of_shared_bed', models.IntegerField(default=1)),
                ('number_of_single_bed', models.IntegerField(default=1)),
                ('bath_number', models.DecimalField(max_digits=3, decimal_places=1)),
                ('utilities', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('picture', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('bedroom', models.TextField(default='Single')),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('deposit', models.DecimalField(max_digits=6, decimal_places=2)),
                ('bounty', models.DecimalField(null=True, max_digits=6, blank=True, decimal_places=2)),
                ('availability', models.DateField()),
                ('video', models.TextField(null=True, blank=True)),
                ('amenity', models.ManyToManyField(to='sell.Amenity')),
                ('owner', models.ForeignKey(to='homepage.Users')),
                ('pictures', models.ManyToManyField(to='sell.Picture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='posting',
            name='amenitiy',
        ),
        migrations.RemoveField(
            model_name='posting',
            name='availability',
        ),
        migrations.DeleteModel(
            name='Availability',
        ),
        migrations.DeleteModel(
            name='Posting',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('time_sent', models.DateTimeField()),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=True)),
                ('from_user', models.ForeignKey(to='homepage.Users', related_name='from_user')),
                ('to_user', models.ForeignKey(to='homepage.Users', related_name='to_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('search', models.TextField()),
                ('user', models.ForeignKey(to='homepage.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

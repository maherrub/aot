# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SaluteList',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=6, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsrProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usercover', models.FileField(upload_to='profile_pictures/', blank=True)),
                ('usermobile', models.DecimalField(max_digits=8, decimal_places=0, blank=True)),
                ('dob', models.DateField(default='1920-01-01')),
                ('salutation', models.OneToOneField(blank=True, to='devup.SaluteList')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usercover', models.FileField(upload_to='profile_pictures/', blank=True)),
                ('usermobile', models.DecimalField(max_digits=8, decimal_places=0, blank=True)),
                ('dob', models.DateField(default='1920-01-01')),
            ],
        ),
        migrations.CreateModel(
            name='UserSalute',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=6, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='salutation',
            field=models.OneToOneField(blank=True, to='usermanager.UserSalute'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]

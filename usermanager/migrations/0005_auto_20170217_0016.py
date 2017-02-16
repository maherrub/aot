# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usermanager', '0004_auto_20170216_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsrProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usercover', models.FileField(upload_to='profile_pictures/', blank=True)),
                ('usermobile', models.DecimalField(max_digits=8, decimal_places=0, blank=True)),
                ('dob', models.DateField(default='1920-01-01')),
            ],
        ),
        migrations.RenameModel(
            old_name='SalutationList',
            new_name='SaluteList',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='salutation',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='usrprofile',
            name='salutation',
            field=models.OneToOneField(blank=True, to='usermanager.SaluteList'),
        ),
        migrations.AddField(
            model_name='usrprofile',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]

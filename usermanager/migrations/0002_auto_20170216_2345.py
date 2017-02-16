# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalutationList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=6, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='edited_on',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default='01-01-1920'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='salutation',
            field=models.OneToOneField(blank=True, to='usermanager.SalutationList'),
        ),
    ]

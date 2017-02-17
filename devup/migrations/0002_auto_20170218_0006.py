# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usrprofile',
            name='firstname',
            field=models.CharField(max_length=25, blank=True),
        ),
        migrations.AddField(
            model_name='usrprofile',
            name='lastname',
            field=models.CharField(max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='usrprofile',
            name='salutation',
            field=models.IntegerField(default=1, max_length=2, choices=[(1, b'Mr'), (2, b'Mrs'), (3, b'Ms'), (4, b'Mdm'), (5, b'Dr'), (6, b'Past'), (7, b'Evan'), (8, b'Prof'), (9, b'Master')]),
        ),
        migrations.DeleteModel(
            name='SaluteList',
        ),
    ]

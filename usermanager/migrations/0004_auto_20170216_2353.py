# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0003_auto_20170216_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salutationlist',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]

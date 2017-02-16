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
                ('salutation', models.CharField(blank=True, max_length=2, choices=[(1, b'Master'), (2, b'Mr'), (3, b'Ms'), (4, b'Mdm'), (5, b'Dr'), (6, b'Past'), (7, b'Evan'), (8, b'Prof')])),
                ('usercover', models.FileField(upload_to=b'profile_pictures/', blank=True)),
                ('usermobile', models.DecimalField(max_digits=8, decimal_places=0, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

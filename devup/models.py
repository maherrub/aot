from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from multiselectfield import MultiSelectField
from django.db import models
import datetime
from devup.choices import SALUTATION_LIST
# Create your models here.

#class SaluteList(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=6, blank=True)

#    def __str__(self):
#        return self.name

class UsrProfile(models.Model):
       
    user = models.ForeignKey(User, default=1)
    salutation = models.IntegerField(max_length=2, choices=SALUTATION_LIST, default=1)  
    firstname = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    usercover = models.FileField(upload_to='profile_pictures/', blank=True)
    usermobile = models.IntegerField(max_length=8,blank=True)
    dob = models.DateField(default='1920-01-01',)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('devup:detail', kwargs={'pk': self.pkb})

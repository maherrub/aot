from django.contrib import admin
from usermanager.models import UserProfile, UserSalute

# Register your models here.
admin.site.register(UserProfile) 
admin.site.register(UserSalute)
from django import forms
from django.contrib.auth.models import User
from usermanager.models import UsrProfile




class UserForm1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class UserForm2(forms.ModelForm):

    class Meta:
        model = UsrProfile
        fields = ['salutation', 'usercover', 'usermobile',]



        
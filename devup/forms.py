from django import forms
from django.forms.extras import SelectDateWidget
from django.contrib.auth.models import User
from devup.models import UsrProfile
from devup.choices import SALUTATION_LIST
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})



class UsrProfileForm(forms.ModelForm):
    salutation = forms.ChoiceField(choices = SALUTATION_LIST,required=True)
    dob = forms.DateField(widget=DateInput())


    class Meta:
        model = UsrProfile
       
        fields = [
            'salutation',
            'firstname', 
            'lastname', 
            'usercover', 
            'usermobile', 
            'dob',
            ]
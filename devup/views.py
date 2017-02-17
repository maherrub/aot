from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.http import HttpRequest 
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from multiselectfield import MultiSelectField

#devup imports
from devup.models import UsrProfile
from devup.forms import UsrProfileForm
from devup.choices import SALUTATION_LIST

#definitions
app_name = 'devup'


#file types
AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.
# Main views below ListView, DetailView, CreateView, UpdateView

class UpList(ListView):

    model = UsrProfile
    template_name_suffix = '_list' or '_menu'

    def dispatch(self, *args, **kwargs):
        return super(UpList, self).dispatch(*args, **kwargs)

class UpDetail(DetailView):

    model = UsrProfile

    def dispatch(self, *args, **kwargs):
        return super(UpDetail, self).dispatch(*args, **kwargs)

class UpCreate(CreateView):

    model = UsrProfile
    form_class = UsrProfileForm

    def dispatch(self, *args, **kwargs):
        return super(UpCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.usercover = self.request.FILES['usercover']
        file_type = self.object.usercover.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'UsrProfile' : UsrProfile,
                'form' : form,
                'error_message' : 'Square Image must be PNG, JPG, or JPEG',
            }
            return redirect(self.object, '/usrprofile_form.html', context)
        self.object.save()
        return redirect(self.object)

class UpUpdate(UpdateView):

    model = UsrProfile
    form_class = UsrProfileForm
    template_name_suffix = '_update'

    def dispatch(self, *args, **kwargs):
        return super(UpUpdate, self).dispatch(*args, **kwargs)













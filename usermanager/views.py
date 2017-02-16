from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from .models import Uprofile
from .forms import UprofileForm, UserForm


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.


from django.shortcuts import render
from .models import project
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    producto= project.objects.all()
    return render(request,'home.html',{'producto': producto})

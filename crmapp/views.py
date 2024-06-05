from django.shortcuts import render,redirect,get_object_or_404
from . models import*
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
def home(request):
   
    
    return render(request, 'home.html')
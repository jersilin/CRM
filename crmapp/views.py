from django.shortcuts import render,redirect,get_object_or_404
from . models import*
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
def home(request):
   return render(request, 'home.html')

def dashboard(request):
   return render(request, 'dashboard.html')

def archieve(request):
   return render(request, 'archieve.html')

def landing(request):
   return render(request, 'landing.html')
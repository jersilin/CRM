from django.urls import path
from . import views
urlpatterns = [
    path('',views.landing,name='landing'),
    path('home',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('archieve',views.archieve,name='archieve'),
    
]
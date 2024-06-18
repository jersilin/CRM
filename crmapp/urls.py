from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('archieve',views.archieve,name='archieve'),
    path('landing',views.landing,name='landing'),
]
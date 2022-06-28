from turtle import home
from xml.etree.ElementInclude import include
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name = 'contact'),
    path('home/', views.home, name='home'),
    path('signup/', views.save, name='SignUp'),
    path('login/', views.signin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
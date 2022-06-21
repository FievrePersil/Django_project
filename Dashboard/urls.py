from turtle import home
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name = 'contact'),
    path('home/', views.home, name='home'),
    path('about/',views.about, name='about')
]
import email
from re import template
from unittest import loader
from django import views
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader

from .models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'index.html')



def save(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        email2 = request.POST['emailAdress']
        phone3 = request.POST['phone']
        password2 = request.POST['password']
        client = User(username=username2, email=email2, password=password2, myphone=phone3)
        client.save()
    return render(request, 'login.html')


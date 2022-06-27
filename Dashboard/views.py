import email
from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from re import template
from telnetlib import AUTHENTICATION
from unittest import loader
from django import views
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from Dashboard import forms

from .models import Utilisateur
from django.contrib.auth import login
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
        client = Utilisateur(username=username2, email=email2, password=password2, myphone=phone3)
        client.save()
        return redirect ('home')
    return render(request, 'login.html')
def signin(request):
    if request.method == 'POST':
        username3 = request.POST['loginemail']
        password3 = request.POST['loginPassword']
        try:
            user = Utilisateur.objects.get(username = username3)
            if user.password == password3:
                return redirect ('home')
        except Utilisateur.DoesNotExist:
            return redirect ('login')
    return render (request, 'login.html')
    
        

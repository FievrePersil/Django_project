from ast import Num
import email
from email import message
from imaplib import _Authenticator
from multiprocessing import AuthenticationError, dummy
from pydoc import cli
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

from .models import Contact, Utilisateur, Voyage
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, 'index.html')

def save(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        email2 = request.POST['email']
        phone3 = request.POST['phone']
        password2 = request.POST['password']
        client = Utilisateur(username=username2, email=email2, password=password2, myphone=phone3)
        client.save()
        return redirect ('login')
    return render(request, 'signup.html')


def contact(request):
    if 'Utilisateur' in request.session:
        current_user = request.session['Utilisateur']
        param = {'current_user': current_user}
        if request.method == 'POST':
            email1 = request.POST['contemail']
            #num1 = Contact.objects.get(email = email1)
            cli = Utilisateur.objects.get(email = email1)
            phonecont = request.POST['contphone']
            message1 = request.POST['message']
            cont = Contact(mail = email1, phone = phonecont, msg = message1, client = cli)
            cont.save()
            return HttpResponse('form sent!')
        return render(request, 'contact.html', param)

    else:
        return redirect('login')
def home(request):
    return render(request, 'index.html')

def profile(request):
    if 'Utilisateur' in request.session:
        current_user = request.session['Utilisateur']
        param = {'current_user': current_user}
        return render(request, 'profile.html', param)
    else:
        return redirect('login')
    return render(request, 'signin.html')




def signin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        check_user = Utilisateur.objects.filter(username=uname, password=pwd)
        if check_user:
            #start a session for the current user
            request.session['Utilisateur'] = uname
            return redirect('profile')
        else:
            return redirect('profile')

    return render(request, 'signin.html')

        
def logout(request):
    try:
        del request.session['Utilisateur']
    except:
        return redirect('login')
    return redirect('login')

def flights(request):
    data = Voyage.objects.all()
    return render (request, 'flights.html', {'voy': data})
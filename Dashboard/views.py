from ast import Num
import email
from email import message
from hmac import trans_36
from imaplib import _Authenticator
from logging import error
from multiprocessing import AuthenticationError, dummy
from platform import uname
from pydoc import cli
from re import template
from telnetlib import AUTHENTICATION
from unittest import loader
from urllib import request
from django import views
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Now
import os
import pdfkit

from Dashboard import forms

from .models import Contact, Reserve, Utilisateur, Voyage
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
            msg = "Wrong Username or password!"
            return render(request, 'signin.html', {'msg': msg})

    return render(request, 'signin.html')

def reservations(request):
    if 'Utilisateur' in request.session:
        uname2 = request.session['Utilisateur']
        c = Utilisateur.objects.get(username = uname2)
        reserve = Reserve.objects.filter(client = c)
        if request.method == 'GET':
            voyageid = request.GET.get('voyid')
            if voyageid is not None:
                v = Voyage.objects.get(voyid = voyageid)
                r = Reserve(client = c, voy = v)
                r.save()
        return render (request, 'reservation.html', {'reserve': reserve, 'uname2':uname2})
    else:
        return render(request, 'signin.html')

def profile(request):
    if 'Utilisateur' in request.session:
        current_user = request.session['Utilisateur']
        param = {'current_user': current_user}
        return render(request, 'profile.html', param)
    else:
        return redirect('login')
    return render(request, 'signin.html')


def logout(request):
    try:
        del request.session['Utilisateur']
    except:
        return redirect('login')
    return redirect('login')

def flights(request):
    data = Voyage.objects.filter(datedep__gt=Now()) #filter only the trips that are not expired
    if 'Utilisateur' in request.session: 
        #if the user is logged in the logo in the page will take me to the profile
        current = request.session['Utilisateur']
        return render (request, 'flights.html', { 'current':current, 'voy': data})
    return render (request, 'flights.html', {'voy': data})

def ticket(request):
    if 'Utilisateur' in request.session:
        uname2 = request.session['Utilisateur']
        c = Utilisateur.objects.get(username = uname2)
        if request.method == 'GET':
            voyageid = request.GET.get('voyid2')
            if voyageid is not None:
                v = Voyage.objects.get(voyid = voyageid)
                reserve = Reserve.objects.get(client = c, voy = v)
                r = reserve.voy.depart
                r2 = reserve.voy.destination
        return render (request, 'ticket.html', {'reserve': reserve, 'uname2':uname2, 'r':r.split('-')[1][0:3], 'r2':r2.split('-')[1][0:3]})
        #up above i splitted the string in two and then i took only the 3 first letters of the second part
    else:
        return HttpResponse('Wrong path please login or make a booking before you request a ticket!')

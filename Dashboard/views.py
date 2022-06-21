from re import template
from unittest import loader
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
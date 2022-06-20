from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'index.html')
from multiprocessing.connection import Client
from django.contrib import admin
from .models import Utilisateur
# Register your models here.
admin.site.register(Utilisateur)
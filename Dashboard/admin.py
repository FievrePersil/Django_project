from multiprocessing.connection import Client
from django.contrib import admin
from .models import Contact, Utilisateur, Voyage
# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Contact)
admin.site.register(Voyage)
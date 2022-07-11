from multiprocessing.connection import Client
from django.contrib import admin
from .models import Avion, Contact,Reserve, Utilisateur, Voyage
# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Contact)
admin.site.register(Voyage)
admin.site.register(Avion)
admin.site.register(Reserve)


from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import EmailField, PasswordInput

# Create your models here.

class Utilisateur(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    myphone = models.CharField(max_length=80)
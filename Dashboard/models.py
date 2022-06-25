from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import EmailField, PasswordInput

# Create your models here.
class Client(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    slug = models.SlugField()
    
    #use it later for reservations
    #date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.username
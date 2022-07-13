import email
from enum import auto
from http import client
from pyexpat import model
from random import random
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.forms import EmailField, PasswordInput
from django.contrib.auth.models import User

# Create your models here.

class Utilisateur(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    myphone = models.CharField(max_length=80)

class Avion(models.Model):
    nomav = models.CharField(max_length=30, primary_key = True)
    modelav = models.CharField(max_length=30)
    capacite = models.IntegerField()
    def __str__(self):
        return self.nomav

class Voyage(models.Model):
    voyid = models.CharField(max_length=20, primary_key= True)
    depart = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    datedep = models.DateTimeField()
    avion = models.ForeignKey("Avion", on_delete=models.CASCADE)
    def __str__(self):
        return self.voyid


class Contact(models.Model):
    #creating an automatic field using a function called build_id
    num = models.AutoField(primary_key=True, auto_created=True)
    mail = models.EmailField()
    phone = models.CharField(max_length=15)
    msg = models.CharField(max_length=150)
    client = models.ForeignKey("Utilisateur", on_delete=models.CASCADE)

class Reserve(models.Model):
    client = models.ForeignKey("Utilisateur", on_delete=models.CASCADE)
    voy = models.ForeignKey("Voyage", on_delete=models.CASCADE)


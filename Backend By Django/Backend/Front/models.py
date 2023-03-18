from django.contrib import admin
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from uuid import uuid4

# Create your models here.

class Parent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    date_of_birth = models.DateField(null=True)

class Child(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length  = 255)
    date_of_birth = models.DateField(max_length  = 255, null=True)
    parent = models.ForeignKey(Parent , on_delete= models.CASCADE)

class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    media_name = models.CharField(max_length  = 255)
    link = models.CharField(max_length  = 255, null=True)
    child = models.ForeignKey(Child , on_delete= models.CASCADE)

class Activity(models.Model):

    ACTIVITY_TEXT = 'T'
    ACTIVITY_IMAGE = 'I'
    ACTIVITY_VOCAL = 'V'

    ACTIVITY_TYPE = [ (ACTIVITY_TEXT, 'TEXT'), (ACTIVITY_IMAGE, 'IMAGE'), (ACTIVITY_VOCAL, 'VOCAL')]

    media_name = models.CharField(max_length  = 255)
    link = models.CharField(max_length  = 255,null=True)
    social_media = models.ForeignKey(Child , on_delete= models.CASCADE)
    message = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=ACTIVITY_TYPE, default=ACTIVITY_TEXT)

class Schedule(models.Model):
    name = models.CharField(max_length  = 255)
    child = models.ForeignKey(Child , on_delete= models.CASCADE)

class Devices(models.Model):
    name = models.CharField(max_length  = 255)
    child = models.ForeignKey(Child , on_delete= models.CASCADE)

class App(models.Model):
    name = models.CharField(max_length  = 255)
    child = models.ForeignKey(Child , on_delete= models.CASCADE)

class Location(models.Model):
    name = models.CharField(max_length  = 255)
    child = models.ForeignKey(Child , on_delete= models.CASCADE)



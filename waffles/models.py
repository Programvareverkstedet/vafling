from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserProfile(AbstractUser):
    pass


class Community(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(UserProfile)


# Jeg har lyst til å vafle!
# Er det noen som er med?
class Listing(models.Model):
    community = models.ForeignKey(Community)
    timeFrom = models.DateTimeField()
    timeTo = models.DateTimeField()
    user = models.ForeignKey(UserProfile)
    description = models.TextField()


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    status = models.BooleanField() # closed - no more edits
    participants = models.ManyToManyField(UserProfile)
    timeFrom = models.DateTimeField()
    timeTo = models.DateTimeField()


class Subevent(models.Model):
    name = models.CharField(max_length=64)
    participants = models.ManyToManyField(UserProfile)
    event = models.ForeignKey(Event)


class ShoppingList(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntField
    payers = models.ManyToManyField(UserProfile)
    subevent = models.ForeignKey(Subevent)



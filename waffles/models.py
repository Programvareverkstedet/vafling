from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserProfile(AbstractUser):
    pass


class Community(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(UserProfile)


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

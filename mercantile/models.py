from django.db import models

from waffles.models import Event, UserProfile


# Create your models here.


class Debt(models.Model):
    amount = models.BigIntegerField()
    debtor = models.ForeignKey(UserProfile, related_name="debtor")
    debtee = models.ForeignKey(UserProfile, related_name="debtee")


# oversikt over oppgjør, for logging
class Calculation(models.Model):
    debt = models.ForeignKey(Debt)
    event = models.ForeignKey(Event)
    date = models.DateTimeField()


# Lagring av oppgjør
class Settlement(models.Model):
    debt = models.ForeignKey(Debt)
    dato = models.DateField()
    amount = models.IntegerField()



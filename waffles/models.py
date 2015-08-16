from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class UserProfile(AbstractUser):
    """
    User profile
    """
    pass

    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')


class Community(models.Model):
    """
    Community

    It works kind of like a django group, but is intended to
    grow more complex over time.
    """
    name = models.CharField(max_length=64, verbose_name=_("Community name"))
    members = models.ManyToManyField(UserProfile, verbose_name=_("Community members"))

    class Meta:
        verbose_name = _('Community')
        verbose_name_plural = _('Communities')


class Listing(models.Model):
    """
    Listing requesting interest in creating an event.

    Supposed to be removed and replaced with an event when someone answers it.
    """
    community = models.ForeignKey(Community, verbose_name=_("Community"))
    timeFrom = models.DateTimeField(verbose_name=_("Start time"))
    timeTo = models.DateTimeField(verbose_name=_("End time"))
    user = models.ForeignKey(UserProfile, verbose_name=_("Requesting user"))
    description = models.TextField(verbose_name=_("Description/text"))

    class Meta:
        verbose_name = _('Listing')
        verbose_name_plural = _('Listing')


class Event(models.Model):
    """
    Event

    A loose collection of participants at a location at a given time
    """
    name = models.CharField(max_length=64, verbose_name=_("Event name"))
    description = models.TextField(verbose_name=_("Description/text"))
    open = models.BooleanField(verbose_name=_("Open for new participants"))
    status = models.BooleanField(verbose_name=_("Finalized"))
    participants = models.ManyToManyField(UserProfile, verbose_name=_("Participants"))
    timeFrom = models.DateTimeField(verbose_name=_("Start time"))
    timeTo = models.DateTimeField(verbose_name=_("End time"))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


class SubEvent(models.Model):
    """
    Used to group parts of an event into smaller groups.

    Used when not everyone is participating in the entire event.
    """
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    participants = models.ManyToManyField(UserProfile, verbose_name=_("Participants"))
    event = models.ForeignKey(Event, verbose_name=_("Parent event"))

    class Meta:
        verbose_name = _('Sub Event')
        verbose_name_plural = _('Sub Events')


class ShoppingList(models.Model):
    """
    Item to be bought or bought to the sub-event

    The reason for using sub-events. Any responsibilities and duties here are isolated within the sub-event.
    """
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    price = models.IntegerField(verbose_name=_("Price"))
    payers = models.ManyToManyField(UserProfile, verbose_name=_("Payers"))
    subevent = models.ForeignKey(SubEvent, verbose_name=_("Connected sub-event"))

    class Meta:
        verbose_name = _('Shopping list')
        verbose_name_plural = _('Shopping lists')

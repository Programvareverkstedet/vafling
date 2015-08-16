from django.contrib import admin

from .models import UserProfile, Community, Event, Listing, ShoppingList, SubEvent


# Register your models here.


@admin.register(UserProfile, Community, Event, Listing, ShoppingList, SubEvent)
class GenericAdmin(admin.ModelAdmin):
    pass

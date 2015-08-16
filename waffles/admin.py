from django.contrib import admin

from .models import UserProfile, Community, Event, Listing, ShoppingList, Subevent


# Register your models here.


@admin.register(UserProfile, Community, Event, Listing, ShoppingList, Subevent)
class GenericAdmin(admin.ModelAdmin):
    pass

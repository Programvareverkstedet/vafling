from django.contrib import admin

from .models import UserProfile, Community, Event


# Register your models here.


@admin.register(UserProfile, Community, Event)
class GenericAdmin(admin.ModelAdmin):
    pass

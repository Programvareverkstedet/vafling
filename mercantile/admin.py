from django.contrib import admin

from .models import Calculation, Debt, Settlement


# Register your models here.


@admin.register(Calculation, Debt, Settlement)
class GenericAdmin(admin.ModelAdmin):
    pass

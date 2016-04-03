from django.contrib import admin

from .models import Drugstore


@admin.register(Drugstore)
class DrugstoreAdmin(admin.ModelAdmin):
    pass

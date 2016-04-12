from django.contrib import admin

from .models import Drugstore, BranchOffice


@admin.register(Drugstore)
class DrugstoreAdmin(admin.ModelAdmin):
    pass


@admin.register(BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    pass

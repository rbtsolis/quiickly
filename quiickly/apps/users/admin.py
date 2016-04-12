from django.contrib import admin

from .models import User, Address, Quiickler


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Quiickler)
class QuiicklerAdmin(admin.ModelAdmin):
    pass

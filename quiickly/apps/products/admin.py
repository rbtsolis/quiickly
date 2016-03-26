from django.contrib import admin

from .models import Brand, Product, Type

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Type)
class ProductAdmin(admin.ModelAdmin):
    pass


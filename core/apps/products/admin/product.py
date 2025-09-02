from django.contrib import admin 

from modeltranslation.admin import TranslationAdmin

from core.apps.products.models import Product, Unity


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'price', 'category']
    list_filter = ['category']


@admin.register(Unity)
class UnityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
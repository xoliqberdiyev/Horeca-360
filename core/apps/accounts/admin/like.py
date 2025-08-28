from django.contrib import admin 

from core.apps.accounts.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']
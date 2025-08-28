from django.contrib import admin 

from core.apps.shared.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'banner']
    
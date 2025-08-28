from django.db import models

from core.apps.shared.models import BaseModel


class Banner(BaseModel):
    banner = models.ImageField(upload_to='shared/banners/')

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'bannerlar'
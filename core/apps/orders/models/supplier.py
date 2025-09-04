from django.db import models

from core.apps.shared.models import BaseModel


class Supplier(BaseModel):
    phone = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    tg_id = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'yetkazib beruvchi'
        verbose_name_plural = 'yetkazib beruvchilar'

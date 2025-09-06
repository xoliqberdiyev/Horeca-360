from django.db import models

from core.apps.shared.models.base import BaseModel



class Category(BaseModel):
    image = models.ImageField(upload_to='products/category/')
    name = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ('order',)


from django.db import models

from core.apps.shared.models.base import BaseModel
from core.apps.products.models import Category


class Unity(BaseModel):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Birlik'
        verbose_name_plural = 'Birliklar'


class Product(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.PositiveBigIntegerField()
    description = models.TextField(null=True, blank=True)
    unity = models.ForeignKey(Unity, on_delete=models.CASCADE, related_name='products', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
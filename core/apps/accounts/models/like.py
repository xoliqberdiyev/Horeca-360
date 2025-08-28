from django.db import models

from core.apps.shared.models import BaseModel
from core.apps.accounts.models import User
from core.apps.products.models import Product


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'likelar'
        verbose_name_plural = 'likelar'
        unique_together = ['user', 'product']

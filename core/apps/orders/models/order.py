from django.db import models

from core.apps.shared.models import BaseModel
from core.apps.accounts.models import User
from core.apps.products.models import Product


class Order(BaseModel):
    PAYMENT_TYPE = (
        ('CASH', 'naqd'),
        ('ACCOUNT_NUMBER', 'hisob raqam'),
    )
    DELIVERY_TYPE = (
        ('YandexGo', 'YandexGo'),
        ('DELIVERY_COURIES', 'kuryer orqali yetkazib berish'),
        ('PICKUP', 'olib ketish'),
    )

    total_price = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders') 
    order_number = models.PositiveBigIntegerField(default=1)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE, null=True)
    delivery_type = models.CharField(max_length=200, choices=DELIVERY_TYPE, null=True)
    delivery_price = models.PositiveBigIntegerField(default=0)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.user} order'

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'
        

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.FloatField()
    price = models.PositiveBigIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items', null=True)

    def __str__(self):
        return f'{self.quantity} - {self.price} to {self.order}'
    
    class Meta:
        verbose_name = 'Buyurtma elementi'
        verbose_name_plural = 'Buyurtma elementlari'
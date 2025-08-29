from django.db import transaction

from rest_framework import serializers

from core.apps.orders.models import Order, OrderItem
from core.apps.products.models import Product


class OrderItemCreateSerializer(serializers.Serializer):
    product_id = serializers.UUIDField()
    quantity = serializers.IntegerField()

    def validate(self, data):
        product = Product.objects.filter(id=data['product_id']).first()
        if not product:
            raise serializers.ValidationError("Product not found")
        data['product'] = product
        data['price'] = product.price * data['quantity']
        return data
    

class OrderCreateSerializer(serializers.Serializer):
    items = OrderItemCreateSerializer(many=True)
    
    def create(self, validated_data):
        with transaction.atomic():
            order_items = validated_data.pop('items')
            order = Order.objects.create(
                user=self.context.get('user'),
            )
            items = []
            total_price = 0
            for item in order_items:
                items.append(OrderItem(
                    product=item.get('product'),
                    price=item.get('price'),
                    quantity=item.get('quantity'),
                    order=order,
                ))
                total_price += item.get('price')
            OrderItem.objects.bulk_create(items)
            order.total_price = total_price
            order.save()
            return order
                
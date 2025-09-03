from rest_framework import serializers

from core.apps.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'total_price', 'user'
        ]
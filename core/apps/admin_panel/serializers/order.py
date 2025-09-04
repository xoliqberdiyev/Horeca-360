from rest_framework import serializers

from core.apps.orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField(method_name='get_product')

    class Meta:
        model = OrderItem
        fields = [
            'id', 'quantity', 'price', 'product',
        ]

    def get_product(self, obj):
        return {
            'id': obj.product.id,
            'name_uz': obj.product.name_uz,
            'name_ru': obj.product.name_ru,
        }


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'total_price', 'user', 'payment_type', 'delivery_type',
            'delivery_price', 'contact_number', 'address', 'comment', 'name', 'items'
        ]

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name,
            'username': obj.user.username
        }
from rest_framework import serializers

from core.apps.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'status', 'total_price', 'user'
        ]

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name,
            'username': obj.user.username
        }
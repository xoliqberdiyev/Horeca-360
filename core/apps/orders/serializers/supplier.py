from rest_framework import serializers

from core.apps.orders.models import Supplier


class SupplierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id', 'phone', 'full_name', 'tg_id'
        ]
from rest_framework import serializers

from core.apps.products.models import Product
from core.apps.accounts.models import Like


class ProductListSerializer(serializers.ModelSerializer):
    liked = serializers.SerializerMethodField(method_name='get_liked')

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'image', 'price', 'description', 'liked'
        ]

    def get_liked(self, obj):
        return Like.objects.filter(user=self.context.get('user'), product=obj).exists()
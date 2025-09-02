from rest_framework import serializers

from core.apps.products.models import Product
from core.apps.accounts.models import Like


class ProductListSerializer(serializers.ModelSerializer):
    liked = serializers.SerializerMethodField(method_name='get_liked')
    unity = serializers.SerializerMethodField(method_name='get_unity')

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'image', 'price', 'description', 'liked', 'unity',
        ]

    def get_liked(self, obj):
        return Like.objects.filter(user=self.context.get('user'), product=obj).exists()
    
    def get_unity(self, obj):
        return {
            'id': obj.unity.id,
            'name': obj.unity.name,
        }
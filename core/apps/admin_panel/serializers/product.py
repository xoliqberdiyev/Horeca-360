from rest_framework import serializers

from core.apps.products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'image', 'category', 'price', 'description', 'unity'
        ]
    
    def get_category(self, obj):
        return {
            'id': obj.category.id,
            'name': obj.category.name
        }

    
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'image', 'category', 'price', 'description', 'unity'
        ]
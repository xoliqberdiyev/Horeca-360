from rest_framework import serializers

from core.apps.products.models import Product


class AdminProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name_uz', 'name_ru', 'image', 'category', 'price', 'description_uz', 'description_ru', 'unity'
        ]
    
    def get_category(self, obj):
        return {
            'id': obj.category.id,
            'name': obj.category.name
        }

    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name_uz', 'name_ru', 'image', 'category', 'price', 'description_uz', 'description_ru', 'unity'
        ]
        extra_kwargs = {
            'image': {'required':False},
            'category': {'required':False},
            'price': {'required':False},
        }


from django.db import transaction

from rest_framework import serializers

from core.apps.orders.models import Order, OrderItem
from core.apps.products.models import Product
from core.apps.products.serializers.product import ProductListSerializer
from core.apps.orders.tasks.order_item import send_orders_to_tg_bot


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
    payment_type = serializers.ChoiceField(choices=Order.PAYMENT_TYPE)
    delivery_type = serializers.ChoiceField(choices=Order.DELIVERY_TYPE)
    delivery_price = serializers.IntegerField(required=False)
    contact_number = serializers.CharField()
    address = serializers.CharField()
    comment = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    
    def create(self, validated_data):
        with transaction.atomic():
            order_items = validated_data.pop('items')
            order = Order.objects.create(
                user=self.context.get('user'),
                payment_type=validated_data.get('payment_type'),
                delivery_type=validated_data.get('delivery_type'),
                delivery_price=validated_data.get('delivery_price'),
                contact_number=validated_data.get('contact_number'),
                address=validated_data.get('address'),
                comment=validated_data.get('comment'),
                name=validated_data.get('name')
            )
            items = []
            total_price = 0
            total_price += validated_data.get('delivery_price')
            for item in order_items:
                items.append(OrderItem(
                    product=item.get('product'),
                    price=item.get('price'),
                    quantity=item.get('quantity'),
                    order=order,
                ))
                total_price += item.get('price')
                send_orders_to_tg_bot.delay(
                    chat_id=item.get('product').tg_id,
                    product_name=item.get('product').name,
                    quantity=item.get('quantity'),
                    price=item.get('price'),
                    payment_type=validated_data.get('payment_type'),
                    delivery_type=validated_data.get('delivery_type'),
                    contact_number=validated_data.get('contact_number'),
                    address=validated_data.get('address'),
                    comment=validated_data.get('comment'),
                    name=validated_data.get('name')
                )

            OrderItem.objects.bulk_create(items)
            order.total_price = total_price
            order.save()
            return order
        

class OrderItemListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = OrderItem
        fields = [
            'id', 'product', 'price', 'quantity', 'created_at'
        ]
                
    
class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemListSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'total_price', 'payment_type', 'delivery_type', 'delivery_price',
            'contact_number', 'address', 'comment', 'name', 'items', 'created_at'
        ]
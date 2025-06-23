from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product


class OrderItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'thumbnail']


class OrderItemSerializer(serializers.ModelSerializer):
    product = OrderItemProductSerializer()
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price', 'subtotal']

    def get_subtotal(self, obj):
        return float(obj.price) * obj.quantity


class OrderListSerializer(serializers.ModelSerializer):
    items_count = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'created_at', 'status', 'total', 'items_count']

    def get_items_count(self, obj):
        return obj.orderitem_set.count()


class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True)
    subtotal = serializers.SerializerMethodField()
    shipping_fee = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'created_at',
            'updated_at',
            'status',
            'shipping_address',
            'notes',
            'items',
            'subtotal',
            'shipping_fee',
            'total',
            'tracking_number',
        ]

    def get_subtotal(self, obj):
        return sum([
            float(item.price) * item.quantity
            for item in obj.orderitem_set.all()
        ])

    def get_shipping_fee(self, obj):
        return 5  # yoki obj.shipping_fee agar modelda mavjud bo‘lsa

    def get_total(self, obj):
        return self.get_subtotal(obj) + self.get_shipping_fee(obj)


# ✅ YETISHMAYOTGAN — OrderCreateSerializer
class OrderItemCreateSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity', 'price']


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ['shipping_address', 'notes', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)

        for item_data in items_data:
            product = Product.objects.get(id=item_data['product_id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item_data['quantity'],
                price=item_data['price']
            )

        return order

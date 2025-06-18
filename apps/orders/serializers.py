from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'created_at', 'status', 'total', 'items_count']
        read_only_fields = ['id', 'order_number', 'created_at', 'total', 'items_count']

from rest_framework import serializers
from .models import Category, Product, Like


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'thumbnail', 'category', 'average_rating', 'likes_count']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'products']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'product', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate(self, attrs):
        user = attrs.get('user')
        product = attrs.get('product')

        if Like.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("You already liked this product.")
        return attrs

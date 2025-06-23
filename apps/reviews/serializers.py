from rest_framework import serializers
from .models import Review
from users.serializers import PublicUserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True, required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ", read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'product_id', 'user', 'rating', 'comment', 'created_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product_id'] = instance.product.id
        return rep

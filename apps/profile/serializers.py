from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'phone',
            'name',
            'email',
            'default_shipping_address',
            'date_joined',
        ]
        read_only_fields = ['id', 'date_joined']


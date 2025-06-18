from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    default_shipping_address = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

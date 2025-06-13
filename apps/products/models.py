from django.db import models
from django.db.models import UniqueConstraint
from apps.common.models import BaseModel
from apps.users.models import User


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_length=10, decimal_places=2)
    thumbnail = models.URLField()  #Products image
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    average_rating = models.FloatField(default=0.0)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'product'], name='unique_user_product_like')
        ]

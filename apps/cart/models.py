from django.db import models
from users.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    items_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user}"

    def update_totals(self):
        items = self.items.all()
        self.total = sum(item.subtotal for item in items)
        self.items_count = sum(item.quantity for item in items)
        self.save()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.product.price
        super().save(*args, **kwargs)
        self.cart.update_totals()
        self.cart.update_totals()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.cart.update_totals()
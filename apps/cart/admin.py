from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'items_count', 'created_at']
    readonly_fields = ['total', 'items_count', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['user__username']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity', 'subtotal']
    readonly_fields = ['subtotal']
    search_fields = ['product__title', 'cart__user__username']
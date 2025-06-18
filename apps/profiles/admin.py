from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'default_shipping_address', 'date_joined')
    search_fields = ('name', 'email', 'phone')

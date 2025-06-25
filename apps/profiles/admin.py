# apps/profiles/admin.py

from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_email', 'phone']

    def get_email(self, obj):
        return obj.user.email if hasattr(obj.user, 'email') else "-"
    get_email.short_description = "Email"

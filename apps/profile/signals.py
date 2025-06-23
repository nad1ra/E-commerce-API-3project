from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        UserProfile.objects.create(
            user=instance,
            phone=getattr(instance, "phone", ""),
            name=getattr(instance, "full_name", "") or getattr(instance, "username", ""),
            email=getattr(instance, "email", ""),
            default_shipping_address=""
        )

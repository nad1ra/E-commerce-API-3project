# Generated by Django 5.2 on 2025-06-24 08:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
        ("reviews", "0002_alter_review_unique_together"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("user", "product")},
        ),
    ]

# Generated by Django 5.2 on 2025-06-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_order_notes_order_shipping_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="tracking_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

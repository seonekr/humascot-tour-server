# Generated by Django 5.0.6 on 2024-06-03 02:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tourApi", "0007_sitemain_imagebannermodel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="guide",
            name="address",
        ),
    ]
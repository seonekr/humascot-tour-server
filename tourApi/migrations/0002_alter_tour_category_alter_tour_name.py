# Generated by Django 5.0.6 on 2024-05-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tourApi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tour",
            name="category",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="tour",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
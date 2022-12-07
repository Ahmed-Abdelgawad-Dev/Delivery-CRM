# Generated by Django 4.1.3 on 2022-12-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0009_alter_customer_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="slug",
        ),
        migrations.AddField(
            model_name="customer",
            name="has_order",
            field=models.BooleanField(default=False),
        ),
    ]
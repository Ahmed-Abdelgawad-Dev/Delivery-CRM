# Generated by Django 4.1.4 on 2022-12-31 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0013_alter_customer_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="customer",
            name="mobile",
            field=models.CharField(max_length=15, unique=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-12 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0012_alter_customer_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

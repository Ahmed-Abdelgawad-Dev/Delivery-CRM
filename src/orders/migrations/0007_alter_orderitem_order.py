# Generated by Django 4.1.3 on 2022-12-23 18:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0006_alter_orderitem_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.order",
            ),
            preserve_default=False,
        ),
    ]
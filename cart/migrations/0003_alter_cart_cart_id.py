# Generated by Django 4.2.1 on 2023-06-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, default='exit', max_length=250),
            preserve_default=False,
        ),
    ]

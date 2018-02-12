# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-02 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cart_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(decimal_places=2, default=25, max_digits=50),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=25, max_digits=50),
        ),
    ]

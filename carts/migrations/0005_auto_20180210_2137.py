# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20180202_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(decimal_places=5, default=0.085, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=25.0, max_digits=50),
        ),
    ]

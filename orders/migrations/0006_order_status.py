# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20180203_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('completed', 'Completed')], default='created', max_length=120),
        ),
    ]

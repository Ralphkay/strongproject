# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-14 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strongholdcoins', '0007_auto_20170914_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]

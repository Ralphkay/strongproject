# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-13 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strongholdcoins', '0004_auto_20170913_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('AW', 'Awaiting Payment'), ('AP', 'Approved'), ('W', 'With Held')], default='AW', max_length=2),
        ),
    ]

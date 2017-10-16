# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-14 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strongholdcoins', '0006_auto_20170913_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bank',
            field=models.CharField(blank=True, choices=[('', 'Select Bank'), ('GT Bank', 'GT BANK'), ('Zenith Bank', 'ZENITH BANK'), ('Stanbic Bank', 'STANBIC BANK'), ('EcoBank', 'ECOBANK'), ('UniBank', 'UNIBANK'), ('Cal Bank', 'CAL BANK')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile_money_vendor',
            field=models.CharField(blank=True, choices=[('MTN', 'MTN'), ('VODAFONE', 'VODAFONE'), ('AIRTEL', 'AIRTEL'), ('TIGO', 'TIGO')], default='MTN', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='4576998', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('AMM', 'Mobile Money'), ('BAT', 'Bank Account Transfer')], default='AMM', max_length=4),
        ),
    ]
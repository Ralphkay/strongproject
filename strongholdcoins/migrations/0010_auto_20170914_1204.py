# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-14 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strongholdcoins', '0009_auto_20170914_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dollar_rate', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('btc_amount', models.DecimalField(decimal_places=2, max_digits=99999)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, default='9451720119', max_length=10, unique=True),
        ),
    ]
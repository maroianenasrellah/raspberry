# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 11:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0007_auto_20170404_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 8, 12, 38, 48, 752083)),
        ),
        migrations.AlterField(
            model_name='sale_history',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 8, 12, 38, 48, 753979)),
        ),
        migrations.AlterField(
            model_name='shopping_history',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 8, 12, 38, 48, 753333)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='username',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

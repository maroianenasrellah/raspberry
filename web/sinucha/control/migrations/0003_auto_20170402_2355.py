# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 22:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20170402_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 2, 23, 55, 55, 852622)),
        ),
        migrations.AlterField(
            model_name='sale_history',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 2, 23, 55, 55, 854732)),
        ),
        migrations.AlterField(
            model_name='shopping_history',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 2, 23, 55, 55, 853988)),
        ),
    ]

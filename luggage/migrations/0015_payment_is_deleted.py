# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-20 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luggage', '0014_auto_20161021_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

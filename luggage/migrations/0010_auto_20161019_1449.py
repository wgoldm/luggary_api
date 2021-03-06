# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-19 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('luggage', '0009_auto_20161019_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='code',
        ),
        migrations.AddField(
            model_name='warehouse',
            name='city',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cities.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.PostalCode'),
        ),
    ]

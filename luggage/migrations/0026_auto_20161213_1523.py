# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-13 12:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models, transaction

@transaction.atomic  # Django 1.6
def import_data(apps, schema_editor):
    Order = apps.get_model("luggage", "Order")

    for o in Order.objects.all():
        o.date_start = o.date_added
        o.date_end = o.date_start + datetime.timedelta(days=o.days)
        o.save()


class Migration(migrations.Migration):

    dependencies = [
        ('luggage', '0025_auto_20161213_1519'),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
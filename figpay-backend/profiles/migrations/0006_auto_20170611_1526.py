# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170610_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='facebook_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='vendor',
            name='facebook_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

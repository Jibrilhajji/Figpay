# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20170610_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('vi', 'Visa'), ('ap', 'BoC API')], default='ap', max_length=2),
        ),
    ]
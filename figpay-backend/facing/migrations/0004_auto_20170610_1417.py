# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facing', '0003_auto_20170610_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='image_1',
            field=models.ImageField(upload_to='pos/snaps/'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160415_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='otp',
            field=models.CharField(default='000000', max_length=20),
            preserve_default=False,
        ),
    ]

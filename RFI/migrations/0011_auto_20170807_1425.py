# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFI', '0010_auto_20170801_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='rfi',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='today_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
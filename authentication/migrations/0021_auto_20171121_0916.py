# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-21 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0020_auto_20171120_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='career_readiness',
            field=models.BooleanField(db_column='career_readiness', default=False, verbose_name='career_readiness'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-14 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0004_profile_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education_description',
            field=models.TextField(default=''),
        ),
    ]

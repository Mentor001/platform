# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-23 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0008_auto_20170716_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]

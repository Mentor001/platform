# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-16 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20170715_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='education_description',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mentorship_areas',
        ),
    ]

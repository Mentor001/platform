# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-14 22:54
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0005_profile_education_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mentorship_areas',
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[('no preference', 'No Preference'), ('academic assistance', 'Academic Assistance'),
                         ('emotional support', 'Emotional Support'), ('entrepreneurship', 'Entrepreneurship'),
                         ('career counceling', 'Career Counceling'), ('interview assistance', 'Interview Assistance')],
                default='', max_length=107),
        ),
    ]

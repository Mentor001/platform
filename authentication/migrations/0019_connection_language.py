# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-20 20:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0018_auto_20171023_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python', models.BooleanField(default=False)),
                ('javascript', models.BooleanField(default=False)),
                ('java', models.BooleanField(default=False)),
                ('c_plus_plus', models.BooleanField(db_column='c/c++', default=False, verbose_name='c++')),
                ('R', models.BooleanField(default=False)),
                ('swift', models.BooleanField(default=False)),
                ('android', models.BooleanField(default=False)),
                ('objective_c', models.BooleanField(default=False)),
                ('php', models.BooleanField(default=False)),
                ('ruby', models.BooleanField(default=False)),
                ('sql', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'languages',
            },
        ),
    ]
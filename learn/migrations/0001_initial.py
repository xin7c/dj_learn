# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-08 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('sex', models.CharField(max_length=2)),
                ('age', models.IntegerField()),
            ],
        ),
    ]

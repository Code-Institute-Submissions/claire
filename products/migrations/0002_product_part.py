# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-29 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='part',
            field=models.CharField(default='', max_length=40),
        ),
    ]
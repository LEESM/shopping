# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20160413_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='delivery',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.ManyToManyField(blank=True, to='item.Category'),
        ),
    ]
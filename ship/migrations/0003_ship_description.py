# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0002_auto_20170122_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='description',
            field=models.TextField(default='', verbose_name='Historic overview'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Container unique identifier')),
                ('hazard', models.CharField(choices=[(0, 'No hazard'), (1, 'Fire hazard'), (2, 'Chemical hazard')], max_length=1)),
            ],
            options={
                'verbose_name': 'Container',
                'verbose_name_plural': 'Containers',
            },
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Ship unique identifier')),
                ('arrival_time', models.DateTimeField(verbose_name='Ship arrival time')),
            ],
            options={
                'verbose_name': 'Ship',
                'verbose_name_plural': 'Ships',
            },
        ),
        migrations.AddField(
            model_name='container',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ship.Ship'),
        ),
    ]

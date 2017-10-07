# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pestana',
            fields=[
                ('id_pestana', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('producto', models.CharField(max_length=45)),
            ],
        ),
    ]

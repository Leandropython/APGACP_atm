# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pestana',
            name='descripcion',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='pestana',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pestana',
            name='producto',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]

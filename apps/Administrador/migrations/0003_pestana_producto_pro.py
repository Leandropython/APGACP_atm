# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0002_auto_20170904_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='pestana',
            name='producto_pro',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]

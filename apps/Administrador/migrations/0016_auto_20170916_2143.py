# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0015_casoprueba_atm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pestana',
            name='id_pestana',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

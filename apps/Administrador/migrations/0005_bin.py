# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0004_remove_pestana_producto_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id_Bin', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('Banco', models.CharField(max_length=45)),
            ],
        ),
    ]

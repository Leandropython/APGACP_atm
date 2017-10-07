# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0009_desarrollador_perfil_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='perfil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Administrador.Perfil'),
            preserve_default=False,
        ),
    ]

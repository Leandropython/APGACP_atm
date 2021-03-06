# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0008_estado_iniciativa_tipo_iniciativa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desarrollador',
            fields=[
                ('id_Desarrollador', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=250)),
                ('anexo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id_Perfil', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_Usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('rut', models.CharField(max_length=45)),
                ('contrasena', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=45)),
            ],
        ),
    ]

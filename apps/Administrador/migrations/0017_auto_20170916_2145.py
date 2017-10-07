# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0016_auto_20170916_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='id_ATM',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bin',
            name='id_Bin',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='casoprueba',
            name='id_CasoPrueba',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='desarrollador',
            name='id_Desarrollador',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estado',
            name='id_Estado',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estado_iniciativa',
            name='id_Estado_iniciativa',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='id_Perfil',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipo_iniciativa',
            name='id_Tipo_iniciativa',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_Usuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

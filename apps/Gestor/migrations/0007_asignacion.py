# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0026_casoprueba_trx'),
        ('usuario', '0005_profile_user'),
        ('Gestor', '0006_auto_20171001_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Profile')),
                ('iniciativa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestor.Iniciativa')),
                ('pestanas', models.ManyToManyField(blank=True, null=True, to='Administrador.Pestana')),
            ],
        ),
    ]

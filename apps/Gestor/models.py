# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models

from apps.Administrador.models import Tipo_iniciativa, Desarrollador, Pestana
from django.contrib.auth.models import User
from apps.usuario.models import Profile


# Create your models here.

class Iniciativa(models.Model):
    id_Iniciativa = models.AutoField(primary_key =True)
    nombre = models.CharField(max_length=45, null = True, blank= True)
    cod_iniciativa = models.CharField(max_length=15, null = True, blank= True)
    descripcion = models.CharField(max_length=250, null = True, blank= True)
    tipo_iniciativa = models.ForeignKey(Tipo_iniciativa, null = True, blank= True, on_delete = models.CASCADE)
    estado_iniciativa = models.CharField(max_length=250, null = True, blank= True)
    fecha_inicio = models.DateField('%d/%m/%Y', null = True, blank= True)
    fecha_cierre = models.DateField('%d/%m/%Y', null = True, blank= True)
    fecha_cierre_real = models.DateField('%d/%m/%Y', null = True, blank= True)
    tipo_prueba = models.CharField(max_length=250, null = True, blank= True)
    prueba = models.CharField(max_length=250, null = True, blank= True)
    tipo_desarrollo = models.CharField(max_length = 45, null = True, blank= True)
    observaciones = models.CharField(max_length = 45, null = True, blank= True)
    desarrollador = models.ForeignKey(Desarrollador, null = True, blank= True, on_delete = models.CASCADE)
    def __str__(self):
        return'{} {}'.format(self.cod_iniciativa, self.nombre)

class Asignacion(models.Model):
    iniciativa = models.ForeignKey(Iniciativa, null = True, blank= True)
    certificador = models.ForeignKey(Profile, null = True, blank= True)
    pestanas = models.ManyToManyField(Pestana, null = True, blank= True)

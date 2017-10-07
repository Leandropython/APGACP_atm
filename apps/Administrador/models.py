# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models
# Create your models here.
class Pestana(models.Model):
    id_pestana = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, blank= True)
    producto = models.CharField(max_length=45, blank= True)

    def __str__(self):
        return'{}'.format(self.nombre)

class Bin(models.Model):
    id_Bin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    banco = models.CharField(max_length=45)
    producto = models.CharField(max_length=45)

    def __str__(self):
        return'{}'.format(self.nombre)

class Estado(models.Model):
    id_Estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank =True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return'{}'.format(self.nombre)

class ATM(models.Model):
    id_ATM = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=45)
    Modelo = models.CharField(max_length=45)
    terminal = models.CharField(max_length=45)

    def __str__(self):
        return'{} {} {}'.format(self.Marca, self.Modelo, self.terminal)

class Estado_iniciativa(models.Model):
    id_Estado_iniciativa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250)
    def __str__(self):
        return'{}'.format(self.nombre)



class Tipo_iniciativa(models.Model):
    id_Tipo_iniciativa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250)
    def __str__(self):
        return'{}'.format(self.nombre)

class Desarrollador(models.Model):
    id_Desarrollador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.CharField(max_length=250)
    anexo = models.CharField(max_length=45)
    def __str__(self):
        return'{}'.format(self.nombre)

class Perfil(models.Model):
    id_Perfil = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return'{}'.format(self.nombre)

class Usuario(models.Model):
    id_Usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    rut = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    correo = models.CharField(max_length=50)
    alias = models.CharField(max_length=45)
    perfil = models.ForeignKey(Perfil, null = True, blank= True, on_delete = models.CASCADE)

class CasoPrueba(models.Model):
    id_CasoPrueba = models.AutoField(primary_key=True)
    pestana = models.ForeignKey(Pestana, null = True, blank= True, on_delete = models.CASCADE)
    tipo_prueba = models.CharField(max_length=250)
    ATM = models.ForeignKey(ATM, null = True, blank= True, on_delete = models.CASCADE)
    bin = models.ForeignKey(Bin, null = True, blank= True, on_delete = models.CASCADE)
    trx = models.CharField(max_length=250)
    prueba = models.CharField(max_length=250)
    resultado_esperado = models.CharField(max_length = 500)
    resultado_obtenido = models.CharField(max_length=45, null= True, blank=True)
    estado = models.ForeignKey(Estado, null = True, blank= True, on_delete = models.CASCADE)
    fecha = models.DateField('%d/%m/%Y')
    Observaciones = models.CharField(max_length=45, null= True, blank=True)

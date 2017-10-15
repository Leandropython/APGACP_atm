# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, null = False, blank= True, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50, null = False, blank= True)
    perfil = models.CharField(max_length=50, null = False, blank= True)
    correo = models.CharField(max_length=250, null = False, blank= True)

    def __str__(self):
<<<<<<< HEAD
        return'{}'.format(self.nombre)

class Gestores(models.Model):
    user = models.ForeignKey(User, null = True, blank= True, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50, null = True, blank= True)
    perfil = models.CharField(max_length=50, null = True, blank= True)
    correo = models.CharField(max_length=250, null = True, blank= True)

class Certificadores(models.Model):
    user = models.ForeignKey(User, null = True, blank= True, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50, null = True, blank= True)
    perfil = models.CharField(max_length=50, null = True, blank= True)
    correo = models.CharField(max_length=250, null = True, blank= True)

    def __str__(self):
        return'{}'.format(self.nombre)
=======
        return'{} {}'.format(self.nombre, self.perfil)
>>>>>>> b6eb04bd4fe9cbc0c1688eaf6d6ac796e69d66a8

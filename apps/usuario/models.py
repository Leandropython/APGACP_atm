# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, null = True, blank= True)
    nombre = models.CharField(max_length=50, null = True, blank= True)
    perfil = models.CharField(max_length=50, null = True, blank= True)
    correo = models.CharField(max_length=250, null = True, blank= True)

    def __str__(self):
        return'{}'.format(self.nombre)

# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib import admin

from apps.Administrador.models import Pestana, Bin, Estado, ATM, Estado_iniciativa, Tipo_iniciativa, Desarrollador, Perfil, Usuario, CasoPrueba

# Register your models here.
admin.site.register(Pestana)
admin.site.register(Bin)
admin.site.register(Estado)
admin.site.register(ATM)
admin.site.register(Estado_iniciativa)
admin.site.register(Tipo_iniciativa)
admin.site.register(Desarrollador)
admin.site.register(Perfil)
admin.site.register(Usuario)
admin.site.register(CasoPrueba)

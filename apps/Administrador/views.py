# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from apps.Administrador.forms import binForm, pestanaForm, ATMForm, EstadoForm, Estado_iniciativaForm, Tipo_iniciativaForm, DesarrolladorForm, PerfilForm, UsuarioForm, CPMForm
from apps.Administrador.models import Bin,ATM, Pestana, Estado, CasoPrueba, Tipo_iniciativa, Estado_iniciativa, Usuario, Perfil, Desarrollador
# Create your views here.
def index_administrador(request1):
    return render(request, 'administracion/index.html')

"""def index(request):
    return render(request, 'Login/index.html')"""


def index_administrador(request):
    return render(request, 'administracion/index.html')

def Perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Perfil_listar')
    else:
        form = PerfilForm()
    return render(request, 'administracion/perfil_ingresar.html', {'form': form})

def perfil_list(request):
    perfil = Perfil.objects.all().order_by('id_Perfil')
    contexto = {'perfils':perfil}
    return render(request, 'administracion/perfil_lista.html', contexto)

def perfil_edit(request, id_Perfil):
    perfil = Perfil.objects.get(id_Perfil =id_Perfil)
    if request.method == 'GET':
        form = PerfilForm(instance = perfil)
    else:
        form = PerfilForm(request.POST, instance = perfil)
        if form.is_valid():
            form.save()
        return redirect('administrador:Perfil_listar')
    return render(request, 'administracion/perfil_ingresar.html', {'form': form})

def perfil_delete(request, id_Perfil):
    perfil = Perfil.objects.get(id_Perfil =id_Perfil)
    if request.method == 'POST':
        perfil.delete()
        return redirect('administrador:Perfil_listar')
    return render(request, 'administracion/perfil_delete.html', {'perfil': perfil})

class perfillist(ListView):
    model = Perfil
    template_name = 'administracion/perfil_lista.html'
    paginate_by = 3

def bin_view(request):
    if request.method == 'POST':
        form = binForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Bin_listar')
        paginate_by = 2
    else:
        form = binForm()
    return render(request, 'administracion/bin_ingresar.html', {'form': form})


def bin_list(request):
    bin = Bin.objects.all().order_by('id_Bin')
    contexto = {'bins':bin}
    return render(request, 'administracion/bin_lista.html', contexto)

def bin_edit(request, id_Bin):
    bin = Bin.objects.get(id_Bin =id_Bin)
    if request.method == 'GET':
        form = binForm(instance = bin)
    else:
        form = binForm(request.POST, instance = bin)
        if form.is_valid():
            form.save()
        return redirect('administrador:Bin_listar')
    return render(request, 'administracion/bin_ingresar.html', {'form': form})

def bin_delete(request, id_Bin):
    bin = Bin.objects.get(id_Bin =id_Bin)
    if request.method == 'POST':
        bin.delete()
        return redirect('administrador:Bin_listar')
    return render(request, 'administracion/bin_delete.html', {'bin': bin})

class binlist(ListView):
    model = Bin
    queryset = Bin.objects.filter(nombre='255537')
    template_name = 'administracion/bin_lista.html'
    paginate_by = 2

def ATM_view(request):
    if request.method == 'POST':
        form = ATMForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Atm_listar')
    else:
        form = ATMForm()
    return render(request, 'administracion/ATM_ingresar.html', {'form': form})

def atm_list(request):
    atm = ATM.objects.all().order_by('id_ATM')
    contexto = {'atms':atm}
    return render(request, 'administracion/atm_lista.html', contexto)

def atm_edit(request, id_ATM):
    atm = ATM.objects.get(id_ATM =id_ATM)
    if request.method == 'GET':
        form = ATMForm(instance = atm)
    else:
        form = ATMForm(request.POST, instance = atm)
        if form.is_valid():
            form.save()
        return redirect('administrador:Atm_listar')
    return render(request, 'administracion/ATM_ingresar.html', {'form': form})

def atm_delete(request, id_ATM):
    atm = ATM.objects.get(id_ATM =id_ATM)
    if request.method == 'POST':
        atm.delete()
        return redirect('administrador:Atm_listar')
    return render(request, 'administracion/atm_delete.html', {'atm': atm})

def pestana_view(request):
    if request.method == 'POST':
        form = pestanaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Pestana_listar')
    else:
        form = pestanaForm()
    return render(request, 'administracion/pestana_ingresar.html', {'form': form})

def pestana_list(request):
    pestana = Pestana.objects.all().order_by('id_pestana')
    contexto = {'pestanas':pestana}
    return render(request, 'administracion/pestana_lista.html', contexto)

def pestana_edit(request, id_pestana):
    pestana = Pestana.objects.get(id_pestana =id_pestana)
    if request.method == 'GET':
        form = pestanaForm(instance = pestana)
    else:
        form = pestanaForm(request.POST, instance = pestana)
        if form.is_valid():
            form.save()
        return redirect('administrador:Pestana_listar')
    return render(request, 'administracion/pestana_ingresar.html', {'form': form})

def pestana_delete(request, id_pestana):
    pestana = Pestana.objects.get(id_pestana =id_pestana)
    if request.method == 'POST':
        pestana.delete()
        return redirect('administrador:Pestana_listar')
    return render(request, 'administracion/pestana_delete.html', {'pestana': pestana})

class pestanalist(ListView):
    model = Pestana
    template_name = 'administracion/pestana_lista.html'
    paginate_by = 5

def Estado_view(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Estado_listar')
    else:
        form = EstadoForm()
    return render(request, 'administracion/estado_ingresar.html', {'form': form})

def estado_list(request):
    estado = Estado.objects.all().order_by('id_Estado')
    contexto = {'estados':estado}
    return render(request, 'administracion/estado_lista.html', contexto)

def estado_edit(request, id_Estado):
    estado = Estado.objects.get(id_Estado =id_Estado)
    if request.method == 'GET':
        form = EstadoForm(instance = estado)
    else:
        form = EstadoForm(request.POST, instance = estado)
        if form.is_valid():
            form.save()
        return redirect('administrador:Estado_listar')
    return render(request, 'administracion/estado_ingresar.html', {'form': form})

def estado_delete(request, id_Estado):
    estado = Estado.objects.get(id_Estado =id_Estado)
    if request.method == 'POST':
        estado.delete()
        return redirect('administrador:Estado_listar')
    return render(request, 'administracion/estado_delete.html', {'estado': estado})

def CPM_view(request):
    if request.method == 'POST':
        form = CPMForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Caso_listar')
    else:
        form = CPMForm()
    return render(request, 'administracion/caso_prueba_maestro.html', {'form': form})

def caso_list(request):
    caso = CasoPrueba.objects.all().order_by('id_CasoPrueba')
    contexto = {'casos':caso}
    return render(request, 'administracion/caso_lista.html', contexto)

def caso_edit(request, id_CasoPrueba):
    caso = CasoPrueba.objects.get(id_CasoPrueba =id_CasoPrueba)
    if request.method == 'GET':
        form = CPMForm(instance = caso)
    else:
        form = CPMForm(request.POST, instance = caso)
        if form.is_valid():
            form.save()
        return redirect('administrador:Caso_listar')
    return render(request, 'administracion/caso_prueba_maestro.html', {'form': form})

def caso_delete(request, id_CasoPrueba):
    caso = CasoPrueba.objects.get(id_CasoPrueba =id_CasoPrueba)
    if request.method == 'POST':
        caso.delete()
        return redirect('administrador:Caso_listar')
    return render(request, 'administracion/caso_delete.html', {'caso': caso})


def Tipo_iniciativa_view(request):
    if request.method == 'POST':
        form = Tipo_iniciativaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Tipo_listar')
    else:
        form = Tipo_iniciativaForm()
    return render(request, 'administracion/tipoiniciativa_ingresar.html', {'form': form})
def tipo_list(request):
    tipo= Tipo_iniciativa.objects.all().order_by('id_Tipo_iniciativa')
    contexto = {'tipos':tipo}
    return render(request, 'administracion/tipo_lista.html', contexto)

def tipo_edit(request, id_Tipo_iniciativa):
    tipo = Tipo_iniciativa.objects.get(id_Tipo_iniciativa =id_Tipo_iniciativa)
    if request.method == 'GET':
        form = Tipo_iniciativaForm(instance = tipo)
    else:
        form = Tipo_iniciativaForm(request.POST, instance = tipo)
        if form.is_valid():
            form.save()
        return redirect('administrador:Tipo_listar')
    return render(request, 'administracion/tipoiniciativa_ingresar.html', {'form': form})

def tipo_delete(request, id_Tipo_iniciativa):
    tipo = Tipo_iniciativa.objects.get(id_Tipo_iniciativa =id_Tipo_iniciativa)
    if request.method == 'POST':
        tipo.delete()
        return redirect('administrador:Tipo_listar')
    return render(request, 'administracion/tipo_delete.html', {'tipo': tipo})

def Estado_iniciativa_view(request):
    if request.method == 'POST':
        form = Estado_iniciativaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Estadoi_listar')
    else:
        form = Estado_iniciativaForm()
    return render(request, 'administracion/estado_iniciativa.html', {'form': form})

def estadoi_list(request):
    estadoi= Estado_iniciativa.objects.all().order_by('id_Estado_iniciativa')
    contexto = {'estadois':estadoi}
    return render(request, 'administracion/estadoi_lista.html', contexto)

def estadoi_edit(request, id_Estado_iniciativa):
    estadoi = Estado_iniciativa.objects.get(id_Estado_iniciativa =id_Estado_iniciativa)
    if request.method == 'GET':
        form = Estado_iniciativaForm(instance = estadoi)
    else:
        form = Estado_iniciativaForm(request.POST, instance = estadoi)
        if form.is_valid():
            form.save()
        return redirect('administrador:Estadoi_listar')
    return render(request, 'administracion/estado_iniciativa.html', {'form': form})

def estadoi_delete(request, id_Estado_iniciativa):
    estadoi = Estado_iniciativa.objects.get(id_Estado_iniciativa =id_Estado_iniciativa)
    if request.method == 'POST':
        estadoi.delete()
        return redirect('administrador:Estadoi_listar')
    return render(request, 'administracion/estadoi_delete.html', {'estadoi': estadoi})

def Usuario_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Usuario_listar')
    else:
        form = UsuarioForm()
    return render(request, 'administracion/usuario_crear.html', {'form': form})
def usuario_list(request):
    usuario= Usuario.objects.all().order_by('id_Usuario')
    contexto = {'usuarios':usuario}
    return render(request, 'administracion/usuario_lista.html', contexto)

def usuario_edit(request, id_Usuario):
    usuario = Usuario.objects.get(id_Usuario =id_Usuario)
    if request.method == 'GET':
        form = UsuarioForm(instance = usuario)
    else:
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
        return redirect('administrador:Usuario_listar')
    return render(request, 'administracion/usuario_crear.html', {'form': form})

def usuario_delete(request, id_Usuario):
    usuario = Usuario.objects.get(id_Usuario =id_Usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('administrador:Usuario_listar')
    return render(request, 'administracion/usuario_delete.html', {'usuario': usuario})

def Desarrollador_view(request):
    if request.method == 'POST':
        form = DesarrolladorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('administrador:Desarrollador_listar')
    else:
        form = DesarrolladorForm()
    return render(request, 'administracion/desarrollador_ingresar.html', {'form': form})

def desarrollador_list(request):
    desarrollador= Desarrollador.objects.all().order_by('id_Desarrollador')
    contexto = {'desarrolladors':desarrollador}
    return render(request, 'administracion/desarrollador_lista.html', contexto)

def desarrollador_edit(request, id_Desarrollador):
    desarrollador = Desarrollador.objects.get(id_Desarrollador =id_Desarrollador)
    if request.method == 'GET':
        form = DesarrolladorForm(instance = desarrollador)
    else:
        form = DesarrolladorForm(request.POST, instance = desarrollador)
        if form.is_valid():
            form.save()
        return redirect('administrador:Desarrollador_listar')
    return render(request, 'administracion/desarrollador_ingresar.html', {'form': form})

def desarrollador_delete(request, id_Desarrollador):
    desarrollador = Desarrollador.objects.get(id_Desarrollador =id_Desarrollador)
    if request.method == 'POST':
        desarrollador.delete()
        return redirect('administrador:Desarrollador_listar')
    return render(request, 'administracion/desarrollador_delete.html', {'desarrollador': desarrollador})

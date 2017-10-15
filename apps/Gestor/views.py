from __future__ import unicode_literals
from __future__ import absolute_import

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.Gestor.forms import IniciativaForm, AsignacionForm
from apps.Gestor.models import Iniciativa, Asignacion
from apps.usuario.models import Profile


# Create your views here.
def index_gestor(request):
    return render(request, 'gestion/index.html')

def iniciativa_view(request):
    if request.method == 'POST':
        form = IniciativaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('gestor:Iniciativa_listar')
    else:
        form = IniciativaForm()
    return render(request, 'gestion/iniciativa_ingresar.html', {'form': form})


def iniciativa_list(request):
    iniciativa = Iniciativa.objects.all().order_by('id_Iniciativa')
    contexto = {'iniciativas':iniciativa}
    return render(request, 'gestion/iniciativa_lista.html', contexto)

def iniciativa_edit(request, id_Iniciativa):
    iniciativa = Iniciativa.objects.get(id_Iniciativa =id_Iniciativa)
    if request.method == 'GET':
        form = IniciativaForm(instance = iniciativa)
    else:
        form = IniciativaForm(request.POST, instance = iniciativa)
        if form.is_valid():
            form.save()
        return redirect('gestor:Iniciativa_listar')
    return render(request, 'gestion/iniciativa_ingresar.html', {'form': form})

class iniciativalist(ListView):
    model = Iniciativa
    template_name = 'gestion/iniciativa_lista.html'
    paginate_by = 3

class AsignacionCreate(CreateView):
    model= Asignacion
    second_model= Profile
    template_name = 'gestion/asignacion_ingresar.html'
    form_class = AsignacionForm
    success_url = reverse_lazy('gestor:Asignacion_listar')


def asignacion_list(request):
    asignacion = Asignacion.objects.all().order_by('id')
    contexto = {'asignacions':asignacion}
    return render(request, 'gestion/asignacion_lista.html', contexto)

def asignacion_edit(request, id):
    asignacion = Asignacion.objects.get(id =id)
    if request.method == 'GET':
        form = AsignacionForm(instance = asignacion)
    else:
        form = AsignacionForm(request.POST, instance = asignacion)
        if form.is_valid():
            form.save()
        return redirect('gestor:Asignacion_listar')
    return render(request, 'gestion/asignacion_ingresar.html', {'form': form})

def asignacion_delete(request, id):
    asignacion = Asignacion.objects.get(id =id)
    if request.method == 'POST':
        asignacion.delete()
        return redirect('gestor:Asignacion_listar')
    return render(request, 'gestion/asignacion_delete.html', {'asignacion': asignacion})

class asignacionlist(ListView):
    model = Asignacion
    template_name = 'gestion/asignacion_lista.html'
    paginate_by = 2

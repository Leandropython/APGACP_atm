from __future__ import absolute_import
from django import forms
from apps.Gestor.models import Iniciativa, Asignacion



class IniciativaForm(forms.ModelForm):
    class Meta:
        model = Iniciativa

        fields =[
            'id_Iniciativa',
            'nombre',
            'cod_iniciativa',
            'descripcion',
            'tipo_iniciativa',
            'fecha_inicio',
            'fecha_cierre',
            'tipo_prueba',
            'tipo_desarrollo',
            'observaciones',
            'desarrollador',
            'estado_iniciativa',
        ]
        labels = {

            'id_Iniciativa': 'id_Iniciativa',
            'nombre': 'Nombre Iniciativa',
            'cod_iniciativa': 'Codigo de Iniciativa',
            'descripcion': 'Descripcion de Iniciativa',
            'tipo_iniciativa': 'Tipo de Iniciativa',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_cierre': 'Fecha de Cierre',
            'tipo_prueba': 'Tipo de Flujo',
            'tipo_desarrollo': 'Tipo de Desarrollo',
            'observaciones': 'Observaciones',
            'desarrollador': 'JP Desarrollo',
            'estado_iniciativa': 'Estado de Iniciativa',
        }
        widgets = {
            'id_Iniciativa': forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'cod_iniciativa': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'tipo_iniciativa': forms.Select(attrs={'class':'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'fecha_cierre': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'tipo_prueba': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_desarrollo': forms.TextInput(attrs={'class':'form-control'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),
            'desarrollador': forms.Select(attrs={'class':'form-control'}),
            'estado_iniciativa': forms.HiddenInput(attrs={'class':'form-control', 'value' : 'Nuevo'}),

        }

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion

        fields =[
            'iniciativa',
            'certificador',
            'pestanas',
        ]
        labels = {

            'iniciativa': 'Iniciativas',
            'certificador': 'Certificadores',
            'pestanas': 'Pestanas',
        }
        widgets = {

            'iniciativa': forms.Select(attrs={'class':'form-control'}),
            'certificador': forms.Select(attrs={'class':'form-control'}),
            'pestanas': forms.CheckboxSelectMultiple(),
        }

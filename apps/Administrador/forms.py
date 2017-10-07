from __future__ import absolute_import
from django import forms
from apps.Administrador.models import Bin, Pestana, ATM, Estado, Estado_iniciativa, Tipo_iniciativa, Desarrollador, Perfil, Usuario, CasoPrueba


class binForm(forms.ModelForm):
    class Meta:
        model = Bin

        fields =[
            'id_Bin',
            'nombre',
            'banco',
            'producto',
        ]
        labels = {
            'id_Bin': 'Id_BIN',
            'nombre': 'BIN',
            'banco': 'Banco BIN',
            'producto': 'Tipo de Producto',
        }
        widgets = {
            'id_Bin': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.TextInput(attrs={'class':'form-control'}),
            'producto': forms.TextInput(attrs={'class':'form-control'}),
        }

class pestanaForm(forms.ModelForm):
    class Meta:
        model = Pestana

        fields =[
            'id_pestana',
            'nombre',
            'descripcion',
            'producto',
        ]
        labels = {
            'id_pestana': 'Id_Pestana',
            'nombre': 'Nombre de Pestana',
            'descripcion': 'Descripcion',
            'producto': 'Producto asociado a Pestana',
        }
        widgets = {
            'id_pestana': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'producto': forms.TextInput(attrs={'class':'form-control'}),
        }
class ATMForm(forms.ModelForm):
    class Meta:
        model = ATM

        fields =[
            'id_ATM',
            'Marca',
            'Modelo',
            'terminal',

        ]
        labels = {
            'id_ATM': 'Id_ATM',
            'Marca': 'Marca del ATM',
            'Modelo': 'Modelo del ATM',
            'terminal': 'Numero de Terminal',

        }
        widgets = {
            'id_ATM': forms.TextInput(attrs={'class':'form-control'}),
            'Marca': forms.TextInput(attrs={'class':'form-control'}),
            'Modelo': forms.TextInput(attrs={'class':'form-control'}),
            'terminal': forms.TextInput(attrs={'class':'form-control'}),

        }
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado

        fields =[
            'id_Estado',
            'nombre',
            'descripcion',

        ]
        labels = {
            'id_Estado': 'Id_Estado',
            'nombre': 'Nombre de Nuevo Estado de Caso de Prueba',
            'descripcion': 'Descripcion del Estado',

        }
        widgets = {
            'id_Estado': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            }

class Estado_iniciativaForm(forms.ModelForm):
    class Meta:
        model = Estado_iniciativa

        fields =[
            'id_Estado_iniciativa',
            'nombre',
            'descripcion',

        ]
        labels = {
            'id_Estado_iniciativa': 'id_Estado_iniciativa',
            'nombre': 'Nombre de Nuevo Estado de Iniciativa',
            'descripcion': 'Descripcion',

        }
        widgets = {
            'id_Estado_iniciativa': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            }

class Tipo_iniciativaForm(forms.ModelForm):
    class Meta:
        model = Tipo_iniciativa

        fields =[
            'id_Tipo_iniciativa',
            'nombre',
            'descripcion',

        ]
        labels = {
            'id_Tipo_iniciativa': 'Id_Tipo_de_Iniciativa',
            'nombre': 'Nombre de Nuevo Tipo de Iniciativa',
            'descripcion': 'Descripcion',

        }
        widgets = {
            'id_Tipo_iniciativa': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            }

class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador

        fields =[
            'id_Desarrollador',
            'nombre',
            'apellido',
            'correo',
            'anexo',

        ]
        labels = {
            'id_Desarrollador': 'Id_Tipo_de_Iniciativa',
            'nombre': 'Nombre del Desarrollador',
            'apellido': 'Apellidos',
            'correo': 'Correo Electronico',
            'anexo': 'Anexo',

        }
        widgets = {
            'id_Desarrollador': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'anexo': forms.TextInput(attrs={'class':'form-control'}),
            }
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil

        fields =[
            'id_Perfil',
            'nombre',


        ]
        labels = {
            'id_Perfil': 'Id_Perfil',
            'nombre': 'Nombre del Nuevo Perfil',


        }
        widgets = {
            'id_Perfil': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields =[
            'id_Usuario',
            'nombre',
            'apellido',
            'rut',
            'contrasena',
            'correo',
            'alias',
            'perfil',


        ]
        labels = {
            'id_Usuario': 'id_Usuario',
            'nombre': 'Nombre Usuario',
            'apellido': 'Apellido Usuario',
            'rut': 'RUT',
            'contrasena': 'Contrasena',
            'correo': 'Correo',
            'alias': 'Alias',
            'perfil': 'Perfil',


        }
        widgets = {
            'id_Usuario': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'contrasena': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
            'alias': forms.TextInput(attrs={'class':'form-control'}),
            'perfil': forms.Select(attrs={'class':'form-control'}),
            }

class CPMForm(forms.ModelForm):
    class Meta:
        model = CasoPrueba

        fields =[
            'id_CasoPrueba',
            'pestana',
            'tipo_prueba',
            'ATM',
            'bin',
            'trx',
            'prueba',
            'resultado_esperado',
            'resultado_obtenido',
            'estado',
            'fecha',
            'Observaciones',

            ]
        labels = {
            'id_CasoPrueba': 'Id_CasoPrueba',
            'pestana': 'Seleccione Pestana',
            'tipo_prueba': 'Tipo de Prueba',
            'ATM': 'Seleccione ATM',
            'bin': 'Seleccione BIN',
            'trx': 'Prueba',
            'prueba': 'Descripcion Caso de Prueba',
            'resultado_esperado': 'Resultado Esperado',
            'resultado_obtenido': 'Resultado Obtenido',
            'estado': 'Estado',
            'fecha': 'Fecha',
            'Observaciones': 'Observaciones',


        }
        widgets = {
            'id_CasoPrueba': forms.TextInput(attrs={'class':'form-control'}),
            'pestana' : forms.Select(attrs={'class':'form-control'}),
            'tipo_prueba': forms.TextInput(attrs={'class':'form-control'}),
            'ATM': forms.Select(attrs={'class':'form-control'}),
            'bin': forms.Select(attrs={'class':'form-control'}),
            'trx': forms.Textarea(attrs={'class':'form-control'}),
            'prueba': forms.Textarea(attrs={'class':'form-control'}),
            'resultado_esperado': forms.Textarea(attrs={'class':'form-control'}),
            'resultado_obtenido': forms.HiddenInput(attrs={'class':'form-control'}),
            'estado' : forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'Observaciones': forms.HiddenInput(attrs={'class':'form-control'}),
            }

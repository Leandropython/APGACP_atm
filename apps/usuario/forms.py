from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.usuario.models import Profile, Gestores, Certificadores
class RegistroForm(UserCreationForm):
    class Meta:

        model = User
        fields =[
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields =[

            'nombre',
            'perfil',
            'correo',
        ]
        labels = {
            'nombre': 'Nombre Usuario',
            'perfil': 'Perfil Usuario',
            'correo': 'Correo Usuario',
        }
        widgets = {
<<<<<<< HEAD
            'nombre': forms.HiddenInput(attrs={'class':'form-control', 'id':'texto2'}),
            'perfil': forms.HiddenInput(attrs={'class':'form-control', 'name':'Precio', 'id':'Precio'}),
            'correo': forms.HiddenInput(attrs={'class':'form-control', 'id':'texto4'}),
}

class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestores

        fields =[

            'nombre',
            'perfil',
            'correo',
        ]
        labels = {
            'nombre': 'Nombre Usuario',
            'perfil': 'Perfil Usuario',
            'correo': 'Correo Usuario',
        }
        widgets = {
            'nombre': forms.HiddenInput(attrs={'class':'form-control', 'id':'texto2'}),
            'perfil': forms.HiddenInput(attrs={'class':'form-control', 'name':'Precio', 'id':'Precio'}),
            'correo': forms.HiddenInput(attrs={'class':'form-control', 'id':'texto4'}),
        }

class CertificadoresForm(forms.ModelForm):
    class Meta:
        model = Certificadores

        fields =[

            'nombre',
            'perfil',
            'correo',
        ]
        labels = {
            'nombre': 'Nombre Usuario',
            'perfil': 'Perfil Usuario',
            'correo': 'Correo Usuario',
        }
        widgets = {
            'nombre': forms.HiddenInput(attrs={'class':'form-control', 'id':'texto2'}),
            'perfil': forms.HiddenInput(attrs={'class':'form-control', 'name':'Precio', 'id':'Precio'}),
            'correo': forms.HiddenInput(attrs={'class':'form-control', 'id':'texto4'}),
=======
            'nombre': forms.TextInput(attrs={'class':'form-control', 'id':'texto2'}),
            'perfil': forms.TextInput(attrs={'class':'form-control', 'name':'Precio', 'id':'Precio'}),
            'correo': forms.TextInput(attrs={'class':'form-control', 'id':'texto4'}),
>>>>>>> b6eb04bd4fe9cbc0c1688eaf6d6ac796e69d66a8
        }

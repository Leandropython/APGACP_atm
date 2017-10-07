from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.usuario.models import Profile
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
            'nombre': forms.HiddenInput(attrs={'class':'form-control', 'id':'texto2'}),
            'perfil': forms.HiddenInput(attrs={'class':'form-control', 'name':'Precio', 'id':'Precio'}),
            'correo': forms.HiddenInput(attrs={'class':'form-control', 'id':'texto4'}),
        }

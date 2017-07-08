from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

from apps.inicio.models import Cancha, Equipo, Partido, EventoPartido, Jugador


class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo electronico',
        }


class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = [
            'nombre_cancha', 'direccion_cancha',
        ]
        labels = {
            'nombre_cancha': 'Nombre de la cancha',
            'direccion_cancha': 'Direccion de la cancha',
        }
        widgets = {
            'nombre_cancha': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_cancha': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'nombre_equipo', 'categoria_equipo',
        ]
        labels = {
            'nombre_equipo': 'Nombre del equipo',
            'categoria_equipo': 'Categoria dle equipo',
        }
        widgets = {
            'nombre_equipo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_equipo': forms.Select(attrs={'class': 'form-control'}),
        }


class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = [
            'fecha_partido','hora_inicio','hora_fin','tipo_partido',
            'resultado','estado_partido','cancha','local','visitante'
        ]
        labels = {
            'fecha_partido':'Fecha del partido',
            'hora_inicio':'Hora de inicio',
            'hora_fin':'Hora de finalizacion',
            'tipo_partido': 'Tipo de partido',
            'resultado': 'Resultado',
            'cancha': 'Cancha',
            'local': 'Equipo local',
            'visitante': 'Equipo visitante',
        }
        widgets = {
            'fecha_partido':forms.TextInput(attrs={'class':'form-control'}),
            'hora_inicio':forms.TimeInput(attrs={'class':'form-control'}),
            'hora_fin':forms.TimeInput(attrs={'class':'form-control'}),
            'tipo_partido': forms.Select(attrs={'class': 'form-control'}),
            'resultado': forms.TextInput(attrs={'class':'form-control'}),
            'cancha': forms.Select(attrs={'class':'form-control'}),
            'local': forms.Select(attrs={'class': 'form-control'}),
            'visitante': forms.Select(attrs={'class': 'form-control'}),
        }


class EventoForm(forms.ModelForm):
    class Meta:
        model = EventoPartido
        fields = [
            'partido',
            'tipo_evento',
            'hora_evento',
            'jugador'
        ]
        labels = {
            'partido':'Partido',
            'tipo_evento':'Tipo de evento',
            'hora_evento':'Hora del evento',
            'jugador':'Jugador'

        }
        widgets = {
            'partido': forms.Select(attrs={'class': 'form-control'}),
            'tipo_evento': forms.Select(attrs={'class': 'form-control'}),
            'hora_evento': forms.TimeInput(attrs={'class':'form-control'}),
            'jugador': forms.Select(attrs={'class': 'form-control'}),
        }
class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
            'identificacion',
            'tipo_identifcacion',
            'edad',
            'telefono',
            'perfil',
            'sexo',
            'equipo',
            'usuario'
        ]
        labels = {
            'identificacion':'Identificacion',
            'tipo_identifcacion':'Tipo de identificacion',
            'edad':'Edad',
            'telefono':'Telefono',
            'perfil':'Perfil del jugador',
            'sexo':'Sexo',
            'equipo':'Equipo',
            'usuario':'Usuario'
        }
        widgets = {
            'identificacion' : forms.TextInput(attrs={'class':'form-control'}),
            'tipo_identifcacion' : forms.Select(attrs={'class': 'form-control'}),
            'edad' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),
            'perfil' : forms.TextInput(attrs={'class':'form-control'}),
            'sexo' : forms.Select(attrs={'class': 'form-control'}),
            'equipo' : forms.Select(attrs={'class': 'form-control'}),
            'usuario' : forms.Select(attrs={'class': 'form-control'}),
        }
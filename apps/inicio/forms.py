from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


from apps.inicio.models import Cancha, Equipo, Partido, EventoPartido, Jugador, Torneo, Torneo_Partido, Reserva


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
            'estado_partido': 'Estado del partido',
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
            'estado_partido': forms.Select(attrs={'class':'form-control'}),
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


class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = [
            'tipo_torneo',
            'nombre_torneo',
            'fecha_inicio',
            'fecha_final',
            'premio',
            'estado_torneo',
        ]
        labels = {
            'tipo_torneo' : 'Tipo de torneo',
            'nombre_torneo' : 'Nombre del torneo',
            'fecha_inicio' : 'Fecha de inicio del torneo',
            'fecha_final' : 'Fecha final del torneo',
            'premio' : 'Premios del torneo',
            'estado_torneo' : 'Estado del torneo'
        }
        widgets = {
            'tipo_torneo': forms.Select(attrs={'class': 'form-control'}),
            'nombre_torneo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'form-control'}),
            'fecha_final': forms.DateInput(attrs={'class':'form-control'}),
            'premio': forms.TextInput(attrs={'class':'form-control'}),
            'estado_torneo': forms.Select(attrs={'class': 'form-control'})
        }


class TorneoPartidoForm(forms.ModelForm):
    class Meta:
        model = Torneo_Partido
        fields = [
            'partido',
        ]
        labels = {
            'partido':'Partido',

        }
        widgets = {
            'partido': forms.Select(attrs={'class': 'form-control'}),
        }


HORAS_HABILES = tuple([(i, i) for i in range(0, 24)])

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


class ReservaForm(forms.ModelForm):
    hora_inicio = forms.ChoiceField(choices=HORAS_HABILES,
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    hora_final = forms.ChoiceField(choices=HORAS_HABILES,
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Reserva
        fields = [
            'fecha_reserva',
            'cancha',
            'abono',
        ]
        labels = {
            'fecha_reserva':'Fecha de la reserva',
            'hora_inicio':'Hora de inicio',
            'hora_final':'Hora final',
            'cancha':'Cancha a reservar',
            'abono':'Monto abonado',
        }

        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'class': 'form-control'}),
            'cancha': forms.Select(attrs={'class': 'form-control'}),
            'abono': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def clean(self):
        import datetime

        cleaned_data = super(ReservaForm, self).clean()
        hora_inicio = cleaned_data.get("hora_inicio")
        hora_final= cleaned_data.get("hora_final")
        cancha = cleaned_data.get("cancha")
        fecha_reserva=cleaned_data.get("fecha_reserva")
        reserva = Reserva.objects.filter(cancha=cleaned_data.get("cancha"),
                                         hora_inicio=datetime.time(int(hora_inicio)),
                                         fecha_reserva=cleaned_data.get("fecha_reserva")).exists()
        if reserva:
            raise forms.ValidationError("ya existe una reserva con esta fecha")


    def clean_hora_final(self):
        hora_inicio = self.cleaned_data["hora_inicio"]
        hora_final = self.cleaned_data["hora_final"]
        if hora_final <= hora_inicio:
            raise forms.ValidationError("La hora final no debe ser igual o inferior a la hora de inicio")
        return hora_final


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from apps.inicio.forms import CanchaForm, PartidoForm, EquipoForm, UsuarioForm
from apps.inicio.models import User, Cancha, Equipo, Partido

class CrearUsuario(CreateView):
    model = User
    template_name = 'usuario/usuario_form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('espicouruts:usuarios_listar')

class DetalleCancha(DetailView):
    model = Cancha
    template_name = "cancha/cancha_detalle.html"
    context_object_name = "detalle_cancha"


class ListarCancha(ListView):
    model = Cancha
    template_name = "cancha/cancha_listar.html"
    context_object_name = "canchas"


def CrearCancha(request):
    if request.method == 'POST':
        form = CanchaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('espicourts:canchas_listar')
    else:
        form=CanchaForm()
    return render(request,'cancha/cancha_form.html',{'cancha_form':form})


def EditarCancha(request,id_cancha):
    cancha=Cancha.objects.get(id=id_cancha)
    if request.method == 'GET':
        form = CanchaForm(instance=cancha)
    else:
        form = CanchaForm(request.POST,instance=cancha)
        if form.is_valid():
            form.save()
        return redirect('espicourts:canchas_listar')
    return render(request,'cancha/cancha_form.html',{'cancha_form':form})


class EliminarCancha(DeleteView):
    model = Cancha
    template_name = 'cancha/canchas_eliminar.html'
    success_url = reverse_lazy('inicio:canchas_listar')


class DetalleEquipo(DetailView):
    model = Equipo
    template_name = "equipo/equipo_detalle.html"
    context_object_name = "detalle_equipo"


class ListarEquipo(ListView):
    model = Equipo
    template_name = "equipo/equipo_listar.html"
    context_object_name = "equipos"


def CrearEquipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('espicourts:equipos_listar')
    else:
        form=EquipoForm()
    return render(request,'equipo/equipo_form.html',{'equipo_form':form})


def EditarEquipo(request,id_equipo):
    equipo=Equipo.objects.get(id=id_equipo)
    if request.method == 'GET':
        form = EquipoForm(instance=equipo)
    else:
        form = EquipoForm(request.POST,instance=equipo)
        if form.is_valid():
            form.save()
        return redirect('espicourts:equipos_listar')
    return render(request,'equipo/equipo_form.html',{'equipo_form':form})


class EliminarEquipo(DeleteView):
    model = Equipo
    template_name = 'equipo/equipo_eliminar.html'
    success_url = reverse_lazy('espicourts:equipos_listar')


class DetallePartido(DetailView):
    model = Partido
    template_name = "partido/partido_detalle.html"
    context_object_name = "detalle_partido"


class ListarPartido(ListView):
    model = Partido
    template_name = "partido/partido_listar.html"
    context_object_name = "partidos"


def CrearPartido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('espicourts:partidos_listar')
    else:
        form=PartidoForm()
    return render(request,'partido/partido_form.html',{'partido_form':form})


def EditarPartido(request,id_partido):
    partido=Partido.objects.get(id=id_partido)
    if request.method == 'GET':
        form = PartidoForm(instance=partido)
    else:
        form = PartidoForm(request.POST,instance=partido)
        if form.is_valid():
            form.save()
        return redirect('espicourts:partidos_listar')
    return render(request,'partido/partido_form.html',{'partido_form':form})


class EliminarPartido(DeleteView):
    model = Partido
    template_name = 'partido/partidos_eliminar.html'
    success_url = reverse_lazy('espicourts:partidos_listar')

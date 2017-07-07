from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from apps.inicio.forms import CanchaForm, PartidoForm, EquipoForm, UsuarioForm, EventoForm
from apps.inicio.models import User, Cancha, Equipo, Partido, EventoPartido


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
    template_name = 'partido/partido_eliminar.html'
    success_url = reverse_lazy('espicourts:partidos_listar')


class Login(FormView):
    # Establecemos la plantilla a utilizar
    template_name = 'login.html'
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url = reverse_lazy("espicourts:canchas_listar")

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


class DetalleUsuario(DetailView):
    model = User
    template_name = "usuario/usuario_detalle.html"
    context_object_name = "detalle_usuario"


class ListarUsuario(ListView):
    model = User
    template_name = "usuario/usuario_listar.html"
    context_object_name = "usuarios"


def CrearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('espicourts:usuarios_listar')
    else:
        form=UsuarioForm()
    return render(request,'usuario/usuario_form.html',{'usuario_form':form})


def EditarUsuario(request,id_usuario):
    usuario=User.objects.get(id=id_usuario)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
    else:
        form = UsuarioForm(request.POST,instance=usuario)
        if form.is_valid()  :
            form.save()
        return redirect('espicourts:usuarios_listar')
    return render(request,'usuario/usuario_form.html',{'usuario_form':form})


class EliminarUsuario(DeleteView):
    model = User
    template_name = 'usuario/usuario_eliminar.html'
    success_url = reverse_lazy('espicourts:usuarios_listar')


class DetalleEvento(DetailView):
    model = EventoPartido
    template_name = "eventos_partido/evento_detalle.html"
    context_object_name = "detalle_evento"


class ListarEvento(ListView):
    model = EventoPartido
    template_name = "eventos_partido/evento_listar.html"
    context_object_name = "eventos"


def CrearEvento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('espicourts:eventos_listar'))
    else:
        form=EventoForm()
    return render(request,'eventos_partido/evento_form.html',{'evento_form':form})


def EditarEvento(request,id_evento):
    evento=EventoPartido.objects.get(id=id_evento)
    if request.method == 'GET':
        form = EventoForm(instance=evento)
    else:
        form = EventoForm(request.POST,instance=evento)
        if form.is_valid()  :
            form.save()
        return redirect('espicourts:eventos_listar')
    return render(request,'eventos_partido/evento_form.html',{'evento_form':form})


class EliminarEvento(DeleteView):
    model = EventoPartido
    template_name = 'eventos_partido/evento_eliminar.html'
    success_url = reverse_lazy('espicourts:eventos_listar')
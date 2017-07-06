from django.conf.urls import url

from apps.inicio.views import DetalleCancha, ListarCancha, CrearCancha, EditarCancha, EliminarCancha, DetalleEquipo, \
    ListarEquipo, CrearEquipo, EditarEquipo, EliminarEquipo, CrearPartido, DetallePartido, ListarPartido, \
    EliminarPartido, EditarPartido, CrearUsuario

urlpatterns = [
    url(r'^usuarios_listar', ListarCancha.as_view(), name='usuarios_listar'),
    url(r'^usuarios_crear', CrearUsuario.as_view(), name='usuarios_crear'),
    url(r'^canchas_detalle/(?P<pk>\d+)/$', DetalleCancha.as_view(), name='canchas_detalle'),
    url(r'^canchas_listar', ListarCancha.as_view(), name='canchas_listar'),
    url(r'^canchas_crear', CrearCancha, name='canchas_crear'),
    url(r'^canchas_actualizar/(?P<id_cancha>\d+)/$', EditarCancha,name='canchas_actualizar'),
    url(r'^canchas_eliminar/(?P<pk>\d+)/$', EliminarCancha.as_view(),name='canchas_eliminar'),
    url(r'^equipos_detalle/(?P<pk>\d+)/$', DetalleEquipo.as_view(), name='equipos_detalle'),
    url(r'^equipos_listar', ListarEquipo.as_view(), name='equipos_listar'),
    url(r'^equipos_crear', CrearEquipo, name='equipos_crear'),
    url(r'^equipos_actualizar/(?P<id_equipo>\d+)/$', EditarEquipo,name='equipos_actualizar'),
    url(r'^equipos_eliminar/(?P<pk>\d+)/$', EliminarEquipo.as_view(),name='equipos_eliminar'),
    url(r'^partidos_detalle/(?P<pk>\d+)/$', DetallePartido.as_view(), name='partidos_detalle'),
    url(r'^partidos_listar', ListarPartido.as_view(), name='partidos_listar'),
    url(r'^partidos_crear', CrearPartido, name='partidos_crear'),
    url(r'^partidos_actualizar/(?P<id_partido>\d+)/$', EditarPartido,name='partidos_actualizar'),
    url(r'^partidos_eliminar/(?P<pk>\d+)/$', EliminarPartido.as_view(),name='partidos_eliminar')
]
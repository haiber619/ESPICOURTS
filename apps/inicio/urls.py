from django.conf.urls import url

from apps.inicio.views import DetalleCancha, ListarCancha, CrearCancha, EditarCancha, EliminarCancha, DetalleEquipo, \
    ListarEquipo, CrearEquipo, EditarEquipo, EliminarEquipo, CrearPartido, DetallePartido, ListarPartido, \
    EliminarPartido, EditarPartido, CrearUsuario, DetalleUsuario, ListarUsuario, EliminarUsuario, EditarUsuario, \
    DetalleEvento, ListarEvento, CrearEvento, EditarEvento, EliminarEvento, DetalleJugador, ListarJugador, CrearJugador, \
    EditarJugador, EliminarJugador

urlpatterns = [
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
    url(r'^partidos_eliminar/(?P<pk>\d+)/$', EliminarPartido.as_view(),name='partidos_eliminar'),
    url(r'^usuarios_detalle/(?P<pk>\d+)/$', DetalleUsuario.as_view(), name='usuario_detalle'),
    url(r'^usuarios_listar', ListarUsuario.as_view(), name='usuarios_listar'),
    url(r'^usuarios_crear', CrearUsuario, name='usuarios_crear'),
    url(r'^usuarios_actualizar/(?P<id_usuario>\d+)/$', EditarUsuario,name='usuarios_actualizar'),
    url(r'^usuarios_eliminar/(?P<pk>\d+)/$', EliminarUsuario.as_view(),name='usuarios_eliminar'),
    url(r'^eventos_detalle/(?P<pk>\d+)/$', DetalleEvento.as_view(), name='evento_detalle'),
    url(r'^eventos_listar', ListarEvento.as_view(), name='eventos_listar'),
    url(r'^eventos_crear', CrearEvento, name='eventos_crear'),
    url(r'^eventos_actualizar/(?P<id_evento>\d+)/$', EditarEvento,name='eventos_actualizar'),
    url(r'^eventos_eliminar/(?P<pk>\d+)/$', EliminarEvento.as_view(),name='eventos_eliminar'),
    url(r'^jugadores_detalle/(?P<pk>\d+)/$', DetalleJugador.as_view(), name='jugador_detalle'),
    url(r'^jugadores_listar', ListarJugador.as_view(), name='jugadores_listar'),
    url(r'^jugadores_crear', CrearJugador, name='jugadores_crear'),
    url(r'^jugadores_actualizar/(?P<id_jugador>\d+)/$', EditarJugador,name='jugadores_actualizar'),
    url(r'^jugadores_eliminar/(?P<pk>\d+)/$', EliminarJugador.as_view(),name='jugadores_eliminar'),
]
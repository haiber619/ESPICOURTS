from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.inicio.views import DetalleCancha, ListarCancha, CrearCancha, EditarCancha, EliminarCancha, DetalleEquipo, \
    ListarEquipo, CrearEquipo, EditarEquipo, EliminarEquipo, CrearPartido, DetallePartido, ListarPartido, \
    EliminarPartido, EditarPartido, CrearUsuario, DetalleUsuario, ListarUsuario, EliminarUsuario, EditarUsuario, \
    DetalleEvento, ListarEvento, CrearEvento, EditarEvento, EliminarEvento, DetalleJugador, ListarJugador, CrearJugador, \
    EditarJugador, EliminarJugador, DetalleTorneo, ListarTorneo, CrearTorneo, EditarTorneo, EliminarTorneo, Index, \
    DetalleTorneoPartido, CrearTorneoPartido, EditarTorneoPartido, EliminarTorneoPartido, \
    ListarReserva, CrearReserva, EliminarReserva, DetalleReserva, ListarTorneoPartido

urlpatterns = [
    url(r'^index/',Index, name='index'),
    url(r'^canchas_detalle/(?P<pk>\d+)/$',login_required(DetalleCancha.as_view()), name='canchas_detalle'),
    url(r'^canchas_listar', login_required(ListarCancha.as_view()), name='canchas_listar'),
    url(r'^canchas_crear', login_required(CrearCancha), name='canchas_crear'),
    url(r'^canchas_actualizar/(?P<id_cancha>\d+)/$', login_required(EditarCancha),name='canchas_actualizar'),
    url(r'^canchas_eliminar/(?P<pk>\d+)/$', login_required(EliminarCancha.as_view()),name='canchas_eliminar'),
    url(r'^equipos_detalle/(?P<pk>\d+)/$', login_required(DetalleEquipo.as_view()), name='equipos_detalle'),
    url(r'^equipos_listar', login_required(ListarEquipo.as_view()), name='equipos_listar'),
    url(r'^equipos_crear', login_required(CrearEquipo), name='equipos_crear'),
    url(r'^equipos_actualizar/(?P<id_equipo>\d+)/$', login_required(EditarEquipo),name='equipos_actualizar'),
    url(r'^equipos_eliminar/(?P<pk>\d+)/$', login_required(EliminarEquipo.as_view()),name='equipos_eliminar'),
    url(r'^partidos_detalle/(?P<pk>\d+)/$', login_required(DetallePartido.as_view()), name='partidos_detalle'),
    url(r'^partidos_listar', login_required(ListarPartido.as_view()), name='partidos_listar'),
    url(r'^partidos_crear', login_required(CrearPartido), name='partidos_crear'),
    url(r'^partidos_actualizar/(?P<id_partido>\d+)/$', login_required(EditarPartido),name='partidos_actualizar'),
    url(r'^partidos_eliminar/(?P<pk>\d+)/$', login_required(EliminarPartido.as_view()),name='partidos_eliminar'),
    url(r'^usuarios_detalle/(?P<pk>\d+)/$', login_required(DetalleUsuario.as_view()), name='usuario_detalle'),
    url(r'^usuarios_listar', login_required(ListarUsuario.as_view()), name='usuarios_listar'),
    url(r'^usuarios_crear', login_required(CrearUsuario), name='usuarios_crear'),
    url(r'^usuarios_actualizar/(?P<id_usuario>\d+)/$', login_required(EditarUsuario),name='usuarios_actualizar'),
    url(r'^usuarios_eliminar/(?P<pk>\d+)/$', login_required(EliminarUsuario.as_view()),name='usuarios_eliminar'),
    url(r'^eventos_detalle/(?P<pk>\d+)/$', login_required(DetalleEvento.as_view()), name='evento_detalle'),
    url(r'^eventos_listar', login_required(ListarEvento.as_view()), name='eventos_listar'),
    url(r'^eventos_crear', login_required(CrearEvento), name='eventos_crear'),
    url(r'^eventos_actualizar/(?P<id_evento>\d+)/$', login_required(EditarEvento),name='eventos_actualizar'),
    url(r'^eventos_eliminar/(?P<pk>\d+)/$', login_required(EliminarEvento.as_view()),name='eventos_eliminar'),
    url(r'^jugadores_detalle/(?P<pk>\d+)/$', login_required(DetalleJugador.as_view()), name='jugador_detalle'),
    url(r'^jugadores_listar', login_required(ListarJugador.as_view()), name='jugadores_listar'),
    url(r'^jugadores_crear', login_required(CrearJugador), name='jugadores_crear'),
    url(r'^jugadores_actualizar/(?P<id_jugador>\d+)/$', login_required(EditarJugador),name='jugadores_actualizar'),
    url(r'^jugadores_eliminar/(?P<pk>\d+)/$', login_required(EliminarJugador.as_view()),name='jugadores_eliminar'),
    url(r'^torneos_detalle/(?P<pk>\d+)/$', login_required(DetalleTorneo.as_view()), name='torneo_detalle'),
    url(r'^torneos_listar', login_required(ListarTorneo.as_view()), name='torneos_listar'),
    url(r'^torneos_crear', login_required(CrearTorneo), name='torneos_crear'),
    url(r'^torneos_actualizar/(?P<id_torneo>\d+)/$', login_required(EditarTorneo),name='torneos_actualizar'),
    url(r'^torneos_eliminar/(?P<pk>\d+)/$', login_required(EliminarTorneo.as_view()),name='torneos_eliminar'),
    url(r'^torneo_partido_detalle/(?P<pk>\d+)/$', login_required(DetalleTorneoPartido.as_view()), name='torneo_partido_detalle'),
    url(r'^torneo_partido_listar/', ListarTorneoPartido, name='torneo_partido_listar'),
    url(r'^torneo_partido_crear/(?P<id_torneo>\d+)/$', CrearTorneoPartido, name='torneo_partido_crear'),
    url(r'^torneo_partido_actualizar/(?P<id_torneop>\d+)/$', login_required(EditarTorneoPartido),name='torneo_partido_actualizar'),
    url(r'^torneo_partido_eliminar/(?P<pk>\d+)/$', login_required(EliminarTorneoPartido.as_view()),name='torneo_partido_eliminar'),
    url(r'^reservas_detalle/(?P<pk>\d+)/$', login_required(DetalleReserva.as_view()), name='reserva_detalle'),
    url(r'^reservas_listar', login_required(ListarReserva.as_view()), name='reservas_listar'),
    url(r'^reservas_crear', login_required(CrearReserva), name='reservas_crear'),
    url(r'^reservas_eliminar/(?P<pk>\d+)/$', login_required(EliminarReserva.as_view()),name='reservas_eliminar'),

]
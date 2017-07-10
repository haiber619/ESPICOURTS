from django.contrib.auth.models import User
from django.db import models



class Equipo(models.Model):
    nombre_equipo=models.CharField('Nombre del Equipo', max_length=30)
    categorias=((1,'Categoria A'),(2,'Categoria B'),(3,'Categoria C'))
    categoria_equipo=models.SmallIntegerField(choices=categorias)
    class Meta:
        db_table='equipo'
    def __str__(self):
        return  "%s " % (self.nombre_equipo)


class Jugador(models.Model):
    identificacion=models.CharField('Identificacion',max_length=12)
    tidentificaciones=((1,'T.I'),(2,'C.C'),(3,'C.E'))
    tipo_identifcacion=models.SmallIntegerField(choices=tidentificaciones)
    edad=models.IntegerField('Edad')
    telefono=models.CharField('Telefono',max_length=20)
    perfil=models.CharField('Perfil del jugador',max_length=60)
    genero = ((1, 'Masculino'), (2, 'Femenino'))
    sexo = models.SmallIntegerField(choices=genero)
    equipo=models.ForeignKey(Equipo,null=True)
    usuario=models.OneToOneField(User, null=True)
    class Meta:
        db_table='jugador'
    def __str__(self):
        return "%s %i %i %s %s %i %i" % (self.identificacion,self.tipo_identifcacion,
                                         self.edad,self.telefono,self.perfil,self.tipo_usuario,
                                         self.sexo)
class Cancha(models.Model):
    nombre_cancha=models.CharField('Nombre', max_length=30)
    direccion_cancha = models.CharField('Direccion', max_length=60)
    class Meta:
        db_table='cancha'
    def __str__(self):
        return "%s " % (self.nombre_cancha)


class Partido(models.Model):
    fecha_partido=models.DateField()
    hora_inicio=models.TimeField()
    hora_fin = models.TimeField(null=True,blank=True)
    tipos=((1,'Amistoso'),)
    tipo_partido=models.SmallIntegerField(choices=tipos)
    resultado=models.CharField('Resultado',max_length=30,null=True,blank=True)
    estados = ((1, 'No iniciado'), (2, 'En proceso'), (3, 'Finalizado'))
    estado_partido = models.SmallIntegerField(choices=estados)
    cancha=models.ForeignKey(Cancha)
    local=models.ForeignKey(Equipo,related_name='equipo_1',null=True)
    visitante=models.ForeignKey(Equipo,related_name='equipo_2',null=True)
    class Meta:
        db_table='partido'
    def __str__(self):
        """return "%s %s %s %s %s" % (self.fecha_partido,self.hora_inicio,self.hora_fin,
                                self.resultado,self.estado_partido)
        """
        return "%s %s" % (self.id,self.fecha_partido)


class EventoPartido(models.Model):
    partido=models.ForeignKey(Partido)
    eventos=((1,'Marcacion del gol'),(2,'Falta'),(3,'Tarjeta amarilla'),
             (4,'Tarjeta azul'),(5,'Tarjeta roja'),(6,'Cambio de jugador'))
    tipo_evento=models.SmallIntegerField(choices=eventos)
    hora_evento=models.TimeField()
    jugador=models.ForeignKey(User)
    class Meta:
        db_table='eventos_partido'
    def __str__(self):
        return "%s %s %s" % (self.partido,self.tipo_evento,self.hora_evento)


class Torneo(models.Model):
    t_torneo=((1,'T.relampago'),(2,'Campeonato'))
    tipo_torneo=models.SmallIntegerField(choices=t_torneo,null=True)
    nombre_torneo=models.CharField('Nombre torneo',max_length=30)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    premio=models.TextField('Premios',max_length=100)
    estados=((1,'No iniciado'),(2,'En proceso'),(3,'Octavos de final'),(4,'Cuartos de final'),
             (5, 'Semifinales'),(6,'Finales'),(7,'Finalizado'))
    estado_torneo=models.SmallIntegerField(choices=estados)
    class Meta:
        db_table='torneo'
    def __str__(self):
        return "%s " % (self.nombre_torneo)


class Torneo_Partido(models.Model):
    torneo=models.ForeignKey(Torneo)
    partido=models.ForeignKey(Partido)
    class Meta:
        db_table='torneo_partido'
    def __str__(self):
        return "%s %s " % (self.torneo,self.partido)



class Reserva(models.Model):
    fecha_reserva=models.DateField()
    hora_inicio=models.TimeField()
    hora_final = models.TimeField()
    cancha=models.ForeignKey(Cancha)
    usuario=models.ForeignKey(User)
    abono=models.DecimalField(max_digits=6,decimal_places=2)
    estados=((1,'Reservado'),(2,'Disponible'))
    estado_reserva=models.SmallIntegerField(choices=estados)

    class Meta:
        db_table='reserva'
        unique_together = ('hora_inicio', 'cancha')

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.fecha_reserva,self.hora_inicio,
                                         self.hora_final,self.cancha,self.usuario,
                                         self.abono,self.estado_reserva)



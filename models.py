import random
from datetime import date

nombres = ["Juan", "Carlos", "Maria", "Ana", "Luis", "Pedro", "Sofia", "Laura", "Ximena", "Fredy", "Tatiana", "Magaly"]
apellidos = ["Gonzalez", "Tandazo", "Rodriguez", "Lopez", "Martinez", "Garcia", "Sanchez", "Ramirez", "Sarango"]

def nombre_aleatorio():
    return random.choice(nombres)

def apellido_aleatorio():
    return random.choice(apellidos)

class Persona:
    def __init__(self, apellido, cedula, fecha_nacimiento, nacionalidad, nombre, sexo):
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.nombre = nombre
        self.sexo = sexo

class Jugador(Persona):
    def __init__(self, apellido, cedula, fecha_nacimiento, nacionalidad, nombre, sexo, categoria, numero_camisa):
        super().__init__(apellido, cedula, fecha_nacimiento, nacionalidad, nombre, sexo)
        self.categoria = categoria
        self.numero_camisa = numero_camisa

class Arbitro(Persona):
    def __init__(self, apellido, cedula, fecha_nacimiento, nacionalidad, nombre, sexo, anios_experiencia):
        super().__init__(apellido, cedula, fecha_nacimiento, nacionalidad, nombre, sexo)
        self.anios_experiencia = anios_experiencia

class Equipo:
    def __init__(self, barrio, color_uniforme, genero, nombre_equipo, nombre_representante):
        self.barrio = barrio
        self.color_uniforme = color_uniforme
        self.genero = genero
        self.nombre_equipo = nombre_equipo
        self.nombre_representante = nombre_representante

class InscripcionEquipo:
    def __init__(self, fecha_inscripcion, equipo):
        self.fecha_inscripcion = fecha_inscripcion
        self.equipo = equipo

    def registrar_inscripcion(self):
        pass  # Implementar la lógica de inscripción

class InscripcionJugador:
    def __init__(self, fecha_inscripcion, jugador):
        self.fecha_inscripcion = fecha_inscripcion
        self.jugador = jugador

    def registrar_inscripcion(self):
        pass  # Implementar la lógica de inscripción

class NominaEncuentro:
    def __init__(self, titularidad):
        self.titularidad = titularidad

class Amonestacion:
    def __init__(self, color_tarjeta):
        self.color_tarjeta = color_tarjeta

class Puntuacion:
    def __init__(self, puntos_derrota_sin_jugar, puntos_por_empate, puntos_por_perdida, puntos_por_victoria, tabla_posiciones):
        self.puntos_derrota_sin_jugar = puntos_derrota_sin_jugar
        self.puntos_por_empate = puntos_por_empate
        self.puntos_por_perdida = puntos_por_perdida
        self.puntos_por_victoria = puntos_por_victoria
        self.tabla_posiciones = tabla_posiciones

class Disciplina:
    def __init__(self, nombre_disciplina):
        self.nombre_disciplina = nombre_disciplina

class Campeonato:
    def __init__(self, duracion_compromiso, fecha_fin, fecha_inicio, genero, nombre, numero_clasificados_por_grupo, numero_equipos_por_grupo, numero_grupo, disciplina):
        self.duracion_compromiso = duracion_compromiso
        self.fecha_fin = fecha_fin
        self.fecha_inicio = fecha_inicio
        self.genero = genero
        self.nombre = nombre
        self.numero_clasificados_por_grupo = numero_clasificados_por_grupo
        self.numero_equipos_por_grupo = numero_equipos_por_grupo
        self.numero_grupo = numero_grupo
        self.disciplina = disciplina

class ProgramacionJuego:
    def __init__(self, fecha, hora):
        self.fecha = fecha
        self.hora = hora

class Jornada:
    def __init__(self, nombre):
        self.nombre = nombre

class Encuentro:
    def __init__(self, fecha_encuentro, tipo_evento, estado):
        self.fecha_encuentro = fecha_encuentro
        self.tipo_evento = tipo_evento
        self.estado = estado

class Escenario:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

class Resultado:
    def __init__(self, marcador, nombre_goleador):
        self.marcador = marcador
        self.nombre_goleador = nombre_goleador

    def registrar_resultado(self):
        pass  # Implementar la lógica de registrar resultado
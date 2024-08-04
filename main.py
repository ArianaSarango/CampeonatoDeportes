from models import *
import random

def generar_cedula():
    return str(random.randint(1000000000, 9999999999))

# Persona
persona = Persona(apellido_aleatorio(), generar_cedula(), date(1990, 1, 1), "Ecuador", nombre_aleatorio(), True)
print(f"Persona: {persona.nombre} {persona.apellido}")

# Jugador
jugador = Jugador(apellido_aleatorio(), generar_cedula(), date(1995, 5, 10), "Ecuador", nombre_aleatorio(), True, "Senior", 10)
print(f"Jugador: {jugador.nombre} {jugador.apellido}, Número de Camisa: {jugador.numero_camisa}")

# Equipo
equipo = Equipo("Centro", "Rojo", True, "Los Guerreros", f"{nombre_aleatorio()} {apellido_aleatorio()}")
print(f"Equipo: {equipo.nombre_equipo}, Representante: {equipo.nombre_representante}")

# Campeonato
disciplina = Disciplina("Futbol")
campeonato = Campeonato(90, date(2023, 12, 31), date(2023, 1, 1), "Masculino", "Liga Local", 4, 8, 2, disciplina)
print(f"Campeonato: {campeonato.nombre}, Disciplina: {campeonato.disciplina.nombre_disciplina}")
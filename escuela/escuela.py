from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materias
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materias] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante) #append para agregar una wea

    def generar_numero_control(self):
        #L - 2024 - 09- longitud lsita estudiantes +1 + random (o-10000)
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes)+1
        aleatorio = randint(0,10000)

        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control
    
    #NUEVOOOOOO

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_controlp(self, maestro: Maestro):
        ano = maestro.fecha_nacimiento.year
        dia = datetime.now().day
        primeras_letras_nombre = maestro.nombre[:2].upper()
        ultimas_letras_rfc = maestro.rfc[-2:].upper()  # Asegúrate de que esto use rfc
        longitud_mas_uno = len(self.lista_maestros) + 1
        aleatorio = randint(500, 5000)

        numero_controlp = f"M{ano}{dia}{aleatorio}{primeras_letras_nombre}{ultimas_letras_rfc}{longitud_mas_uno}"

        return numero_controlp
    
        #NUEVOOOOO MATERIAAASSSSS
    def registrar_materia(self, materia: Materias):
        self.lista_materias.append(materia)

    def generar_id(self, materia: Materias):
        ultimas_letras_id = materia.nombre[-2:].upper()
        semestre = materia.semestre
        credito = materia.creditos
        aleatorio = randint(1, 1000)

        id_materia = f"MT{ultimas_letras_id}{semestre}{credito}{aleatorio}"
        return id_materia

        

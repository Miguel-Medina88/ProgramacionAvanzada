from typing import List
from estudiantes.estudiante import Estudiante
from materias.materia import Materia
from random import randint

class Grupo:
    id: str
    estudiantes: List[Estudiante] = []
    materias: List[Materia] = []
    tipo: chr
    id_semestre: str

    def __init__(self, tipo: chr, id_semestre: str):
        self.id = self.generar_id()
        self.tipo = tipo
        self.id_semestre = id_semestre

    def generar_id(self, tipo: chr) -> str:
        return f"{tipo}-{randint(0, 100000)}-{randint(0, 100000)}"


    def registrar_estudiante(self, estudiante:Estudiante):
        self.estudiantes.append(estudiante)
    
    def registrar_materia(self, materia:Materia):
        self.materias.append(materia)

    def mostrar_info_grupo_para_estudiante(self):
        print("Informacion del Grupo {self.tipo}, del semestre {self.id_semestre}")
        for materia in self.materias:
            print (materia.mostrar_info_materia())
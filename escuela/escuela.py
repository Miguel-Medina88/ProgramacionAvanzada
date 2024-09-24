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
        print("\nSe registro exitosamente al estudiante con numero de control: ", estudiante.numero_control)

    def generar_numero_control(self):
        #L - 2024 - 09- longitud lsita estudiantes +1 + random (o-10000)
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes)+1
        aleatorio = randint(0,10000)

        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control
    
    def listar_estudiantes(self):
        print("** Estudiante **")    
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control.strip(): #CAMBIEEEEEEEEEE
                self.lista_estudiantes.remove(estudiante)
                print(f"Estudiante {estudiante.nombre} {estudiante.apellido}, eliminado exitosamente.\n")
                return 
            
        print(f"NO se encontro al wey xd con el numero de control: {numero_control}")

    #MAESTROOo0o0o0o0O00o0oS

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def listar_maestros(self):
        print("** Maestros **")    
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestros())

    def generar_numero_controlp(self, maestro: Maestro):
        ano = maestro.fecha_nacimiento.year
        dia = datetime.now().day
        primeras_letras_nombre = maestro.nombre[:2].upper()
        ultimas_letras_rfc = maestro.rfc[-2:].upper()  # Asegúrate de que esto use rfc
        longitud_mas_uno = len(self.lista_maestros) + 1
        aleatorio = randint(500, 5000)
        numero_controlp = f"M{ano}{dia}{aleatorio}{primeras_letras_nombre}{ultimas_letras_rfc}{longitud_mas_uno}"
        return numero_controlp
    
    def eliminar_maestro(self, numero_controlp: str):
        for maestro in self.lista_maestros:
            if maestro.numero_controlp == numero_controlp.strip(): #CAMBIEEEEEEEEEE
                self.lista_maestros.remove(maestro)
                print(f"Maestro {maestro.nombre} {maestro.apellido}, eliminado exitosamente.\n")
                return 
            
        print(f"\nNO se encontro al maestro con el numero de control: {numero_controlp}\n")
    
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

    

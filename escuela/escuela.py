from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materias
from carrera.carrera import Carrera
from semestre.semestre import Semestre 
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materias] = []
    lista_carreras: List[Carrera] = []
    lista_semestre: List[Semestre] = []

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

    def listar_materias(self):
        print("** Materias **")    
        for materias in self.lista_materias:
            print(materias.mostrar_info_materia())

    def eliminar_materia(self, id_materia: str):
        for materia in self.lista_materias:
            if materia.id == id_materia.strip(): #CAMBIEEEEEEEEEE
                self.lista_materias.remove(materia)
                print(f"Materia {materia.nombre}, eliminado exitosamente.\n")
                return 
    
    #carrera
    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)
    
    def listar_carreras(self):
        print("*************Carreras*************")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())
        #SEMESTRE
    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id_carrera
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
        self.lista_semestre.append(semestre)

    def listar_semestres(self):
        print("*************Semestres*************")
        for semestre in self.lista_semestre:
            print(semestre.mostrar_info_semestre())
            
          #GRUPOOOOOS
    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre

        for semestre in self.lista_semestre:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        self.lista_grupos.append(grupo)
    
    def listar_grupos(self):
        print("** Grupos **")   
        for grupo in self.lista_grupos:  # Cambiar a singular para mayor claridad
            print(grupo.mostrar_info_grupo())
        

    
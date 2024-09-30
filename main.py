from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materias
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupo import Grupo
from datetime import datetime

escuela = Escuela()

while True:
    print("** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros")
    print("8. Mostrar materias")
    print("9. Mostrar grupos")
    print("10. Eliminar estudiantes")
    print("11. Eliminar maestros")
    print("12. Eliminar materias")
    print("13. Registrar carrera")
    print("14. Registrar semestre")
    print("15. Mostrar carreras")
    print("16. Mostrar semestres")
    print("17. Mostrar grupos")
    print("19. Salir")
    opcion = input("Ingrese una opcion para continuar pa: ")
    
    if opcion == "1":
        print("\nSeleccionaste agregar un estudiante \n")
        numero_control = escuela.generar_numero_control()
        print("numero de control es: ", numero_control)

        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        estudiante = Estudiante(nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, numero_control=numero_control)
        escuela.registrar_estudiante(estudiante=estudiante)

    elif opcion == "2":
        print("\nSeleccionaste agregar un maestro \n")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa el rfc del maestro: ")
        sueldo = input("Ingresa el sueldo del maestro: ")
        ano = int(input("Ingresa el año de nacimiento del maestro: "))
        mes = int(input("Ingresa el mes de nacimiento del maestro: "))
        dia = int(input("Ingresa el dia de nacimiento del maestro: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        maestro = Maestro("", nombre=nombre, apellido=apellido, sueldo=sueldo, rfc=rfc, fecha_nacimiento=fecha_nacimiento)
        numero_controlp = escuela.generar_numero_controlp(maestro)
        print("Número de control: ", numero_controlp)
        maestro.numero_controlp = numero_controlp
        escuela.registrar_maestro(maestro=maestro)

    elif opcion == "3":
        print("\nSeleccionaste agregar una materia \n")

        nombre = input("Ingrese el nombre de la materia: ")
        descripcion = input("Ingresa una descripcion breve de la materia: ")
        semestre = input("Ingresa el semestre en que se toma la materia: ")
        creditos = input("Ingresa el numero de creditos de la materia: ")
        materia = Materias("", nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
        id_materia = escuela.generar_id(materia)
        print(f"EL ID de la materia es: ", id_materia)
        materia.id = id_materia
        escuela.registrar_materia(materia=materia)

    
    elif opcion == "4":
        print("\nSeleccionaste agregar un grupo \n")
        tipo = input("Ingresa el tipo de grupo A o B: ")
        id_semestre = input ("Ingresa el ID del semestre al que pertenece el grupo: ")

        grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
        escuela.registrar_grupo(grupo=grupo)

    
    elif opcion == "5":
        print("\nSeleccionaste agregar un horario \n")

    elif opcion == "6":
        escuela.listar_estudiantes()

    elif opcion == "7":
        escuela.listar_maestros()

    elif opcion == "8":
        escuela.listar_materias()

    elif opcion == "9":
        escuela.lista_estudiantes

    elif opcion == "10":
        print("\nSeleccionaste la opcion para eliminar un estudiante \n")
        numero_control = input("\nIngresa el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion == "11":
        print("\nSeleccionaste la opcion para eliminar un maestro \n")
        numero_controlp = input("\nIngresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_controlp=numero_controlp)

    elif opcion == "12":
        print("\nSeleccionaste la opcion para eliminar una materia \n")
        id_materia = input("\nIngresa el ID de la materia: ")
        escuela.eliminar_materia(id_materia=id_materia)

    elif opcion == "13":
        print("\nSeleccionaste la opcion para registrar una carrera")

        nombre = input("Ingresa el nombre de la carrera: ")

        carrera = Carrera(nombre=nombre)
        escuela.registrar_carrera(carrera=carrera)

    elif opcion == "14":
        print("\nSeleccionaste la opcion para registrar un semestre")

        numero = input("Ingresa el numero del semestre: ")
        id_carrera = input("Ingresa el ID de la carrera: ")

        semestre = Semestre(numero=numero, id_carrera=id_carrera)
        escuela.registrar_semestre(semestre=semestre)

    elif opcion == "15":
        escuela.listar_carreras()

    elif opcion == "16":
        escuela.listar_semestres()
    
    elif opcion == "17":
        escuela.listar_grupos()



    elif opcion == "19":
        print("\nAdios cara de bola ")
        break

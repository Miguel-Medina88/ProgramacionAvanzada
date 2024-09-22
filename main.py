from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materias
from datetime import datetime

escuela = Escuela()

while True:
    print("** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")
    opcion = input("Ingrese una opcion para continuar pa: ")
    
    if opcion == "1":
        print("\nSeleccionaste agregar un estudiante \n")
        numero_control = escuela.generar_numero_control()
        print("numero de control es: ", numero_control)

        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        crup = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)

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
        print(f"Número de control: ", numero_controlp)
        maestro.numero_controlp = numero_controlp

    elif opcion == "3":
        print("\nSeleccionaste agregar una materia \n")

        nombre = input("Ingrese el nombre de la materia: ")
        descripcion = input("Ingresa una descripcion breve de la materia: ")
        semestre = input("Ingresa el semestre en que se toma la materia: ")
        creditos = input("Ingresa el numero de creditos de la materia: ")
        materia = Materias("", nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
        id_materia = escuela.generar_id(materia)
        print(f"EL ID de la materia es: ", id_materia)
        materia.id = id

    
    elif opcion == "4":
        print("\nSeleccionaste agregar un grupo \n")
    
    elif opcion == "5":
        print("\nSeleccionaste agregar un horario \n")
    
    else:
        print("\nAdios cara de bola ")
        break

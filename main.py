from estudiante import Estudiante
from curso import Curso

curso_uno = Curso("Mecanica de Fluidos", 1, "Eli Chagolla Inzunza")
curso_dos = Curso("Mecanismos", 2, "Fernando Saldaña")
curso_tres = Curso("Electronica", 3, "Anthony Morales Cervantes")

estudiante_uno = Estudiante("Poncho", 18, 1)
estudiante_dos = Estudiante("Beni", 20, 2)

estudiante_uno.agregar_curso(curso_uno)
estudiante_uno.agregar_curso(curso_tres)

estudiante_dos.agregar_curso(curso_uno)
estudiante_dos.agregar_curso(curso_dos)

curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()

estudiante_uno.mostrar_informacion()
estudiante_dos.mostrar_informacion()
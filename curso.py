class Curso:
    nombre_curso = ""
    codigo_curso = 0
    instructor = ""

    def __init__(self, nombre_curso, codigo_curso, instructor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor

    def mostrar_info_curso(self):
        print("\nNombre del Curso: ", self.nombre_curso)
        print("Codigo del Curso: ", self.codigo_curso)
        print("Instructor: ", self.instructor)
        
class Materias:
    id: str
    nombre: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__(self, id: str, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos

    def mostrar_info_materia(self):
        nombre = f"{self.nombre}"
        info = f"Nombre: {nombre}, descripcion: {self.descripcion}, Semestre: {self.semestre}, Creditos: {self.creditos}, ID:{self.id}"
        return info
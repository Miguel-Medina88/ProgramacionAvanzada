from datetime import datetime

class Maestro:
    numero_controlp : str
    nombre : str
    apellido : str
    rfc : str
    sueldo : float
    fecha_nacimiento: datetime

    def __init__(self, numero_controlp: str, nombre: str, apellido: str, sueldo: float, rfc: str, fecha_nacimiento: datetime):
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
        self.numero_controlp = numero_controlp
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info_maestros(self):
        nombre_completo = f"{self.nombre}{self.apellido}"
        info = f"Numero de control: {self.numero_controlp}, nombre completo: {nombre_completo}, sueldo: {self.sueldo},rfc: {self.rfc}, fecha de nacimiento: {self.fecha_nacimiento}"
        return info

#ELIMINAR Y LISTADO MATERIA Y MAESTRO TAREAAAAAAAAAAAAAA!!!!!!!!!!!!!!!!!

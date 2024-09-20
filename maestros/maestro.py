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


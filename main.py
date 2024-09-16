"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2014, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Avenida Madero") # 5
paciente_tres = Paciente("Beni", 2004, 65, 1.72, "Vista bella") 

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8
medico1 = Medico("Carlitos", 1975, "CAR1234ABCD", "Calle Panadera")
medico2 = Medico("Laura", 1980, "LAU5678EFGH", "Pesherman Sydney")

# Registrar los médicos en el hospital
hospital.registrar_medico(medico1)
hospital.registrar_medico(medico2)
hospital.registrar_medico(medico=medico)
hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_paciente(paciente=paciente_tres)

hospital.eliminar_paciente(paciente_dos.id)
hospital.eliminar_medico(medico2.id)

hospital.mostrar_medicos()
hospital.mostrar_pacientes()
hospital.mostrar_pacientes_menores() #nuevo
hospital.mostrar_pacientes_mayores()

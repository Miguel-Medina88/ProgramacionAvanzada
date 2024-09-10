# main.py

from coche import Coche

def main():
    # Crear tres objetos de tipo Coche
    coche1 = Coche("Toyota", "Corolla", 2015)
    coche2 = Coche("Honda", "Civic", 2018)
    coche3 = Coche("Ford", "Focus", 2020)
    
    # Mostrar información de cada coche
    coches = [coche1, coche2, coche3]
    for coche in coches:
        coche.mostrar_informacion()
        print(f"Edad del coche: {coche.calcular_edad_del_coche(2024)} años\n")

if __name__ == "__main__":
    main()

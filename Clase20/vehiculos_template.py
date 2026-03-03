"""
Clase 20 - Herencia: EJERCICIO 1 — Template para alumnos
=========================================================
Archivo: ejercicio1_template.py

Instrucciones:
- Completa las clases siguiendo los comentarios # TODO:
- Vehiculo es la clase PADRE
- Coche y Moto son clases HIJAS que heredan de Vehiculo
- Usa super().__init__() para llamar al constructor del padre
"""


# ============================================================
# Clase padre: Vehiculo
# ============================================================

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año 
        

    def encender(self):
        print (f'El {self.marca} {self.modelo} esta encendido')
        
# ============================================================
# Clase hija: Coche
# Hereda de Vehiculo y agrega: puertas
# ============================================================

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__('Audi', 'TT', '2020')
        self.puertas = puertas 

    def abrir_puerta(self):
        print(f'Abriendo puerta del {self.marca}')
        
# ============================================================
# Clase hija: Moto
# Hereda de Vehiculo y agrega: cilindrada
# ============================================================

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilidrada):
        super().__init__('Honda', 'CBR1000', '2024')
        self.cilidrada = cilidrada

    def hacer_caballito(self):
        print(f"!{self.marca} haciendo caballito")

# ============================================================
# Pruebas — NO modificar esta sección
# Si tu código es correcto, esto debería funcionar sin errores
# ============================================================

if __name__ == "__main__":

    print("Probando Coche...")
    mi_coche = Coche("Toyota", "Corolla", 2022, 4)
    mi_coche.encender()       # El Toyota Corolla está encendido
    mi_coche.abrir_puerta()   # Abriendo puerta del Toyota
    print(f"Puertas: {mi_coche.puertas}")  # 4

    print()

    print("Probando Moto...")
    mi_moto = Moto("Honda", "CBR", 2021, 600)
    mi_moto.encender()          # El Honda CBR está encendido
    mi_moto.hacer_caballito()   # ¡Honda haciendo caballito!
    print(f"Cilindrada: {mi_moto.cilidrada}cc")  # 600cc

    print()

    print("Verificando herencia...")
    print(f"Coche es Vehiculo: {isinstance(mi_coche, Vehiculo)}")  # True
    print(f"Moto es Vehiculo: {isinstance(mi_moto, Vehiculo)}")    # True

    print()
    print("¡Todo correcto!" if isinstance(mi_coche, Vehiculo) else "Revisa la herencia")

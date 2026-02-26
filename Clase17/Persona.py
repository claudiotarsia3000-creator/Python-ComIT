
# Persona.py - Ejercicio de POO Clase 17
# En este ejercicio aprendimos a crear una clase y usar el constructor __init__

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Pruebas manuales (como hicimos en clase)
persona1 = Persona("Juan", 30)
print(persona1.nombre)
print(persona1.edad)

persona2 = Persona("Carlos", 25)
print("Nombre de la segunda persona:", persona2.nombre)

 
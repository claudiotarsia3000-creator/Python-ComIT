class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

ana = Persona("Ana", 30)
carlos = Persona("Carlos", 25)
maria = Persona("Maria", 35)
print(f'{ana.nombre} tiene {ana.edad} años.')
print(f'{carlos.nombre}')

ana.edad = 99
print(ana.edad)
print(carlos.edad)


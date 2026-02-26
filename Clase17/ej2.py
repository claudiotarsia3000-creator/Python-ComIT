class Mascota:
    def __init__(self,nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

mi_perro = Mascota("Firulai", "Perro", 3)
perro_de_Carlos = Mascota("Pichichus", "Perro", 5)
mi_gato = Mascota("Trigo", 'Gato', 4)
mi_pajaro = Mascota ('FlyFly', 'Pajato', 3)

print(f'{mi_perro.nombre} es un {mi_perro.especie} de {mi_perro.edad} años.')

print(f'{mi_gato.nombre} es un {mi_gato.especie} de {mi_gato.edad} años.')

print(f'{mi_pajaro.nombre} es un {mi_pajaro.especie} de {mi_pajaro.edad} años.')

print(f'{perro_de_Carlos.nombre} es un {perro_de_Carlos.especie} de {perro_de_Carlos.edad} años de viejito... ')









# ana = Persona("Ana", 30)
# carlos = Persona("Carlos", 25)
# maria = Persona("Maria", 35)
# print(f'{ana.nombre} tiene {ana.edad} años.')
# print(f'{carlos.nombre}')
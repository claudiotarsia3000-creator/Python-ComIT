class Casa:
    def __init__(self, num_cuartos, num_baños, num_pisos, tipo_de_vivienda):
        self.num_cuartos = num_cuartos
        self.num_baños = num_baños
        self.num_pisos = num_pisos
        self.tipo_de_vivienda = tipo_de_vivienda # Corregido: ahora guarda el texto

# Todas las casas DEBEN tener los 4 datos que pide el __init__
casa1 = Casa(3, 4, 2, 'Casa Pequeña')
casa2 = Casa(4, 2, 2, 'Departamento') # Agregué el tipo
casa3 = Casa(3, 2, 1, 'Cabaña')        # Agregué el tipo

# Corregimos el print para que use los atributos
print(f'La propiedad es una {casa1.tipo_de_vivienda} de {casa1.num_cuartos} cuartos, {casa1.num_baños} baños y {casa1.num_pisos} pisos.')
print(f'Esta propiedad es un {casa2.tipo_de_vivienda} de {casa2.num_cuartos} cuartos, {casa2.num_baños} baños y {casa2.num_pisos} pisos.') 
print(f'Este inmueble, es una {casa3.tipo_de_vivienda}, Cuenta con {casa3.num_cuartos} cuartos, con {casa3.num_baños} baños y esta establecida en {casa3.num_pisos} pisos')


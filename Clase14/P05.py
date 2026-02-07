# Conversor de Lista

def convertir_lista(lista_strings):

    """Convierte lista de strings a numeros, ignorando invalidos."""
    numeros_validos = []
    for item in lista_strings:
        try:
            numero = float(item)
            numeros_validos.append(numero)
        except ValueError:
            print(f"Ignorando valor invalido: '{item}'")
    return numeros_validos

# Pruebas
datos = ["1", "2.5", "hola", "3", "abc", "4.0"]
resultado = convertir_lista(datos)
print(f"Numeros validos: {resultado}")  # [1.0, 2.5, 3.0, 4.0]



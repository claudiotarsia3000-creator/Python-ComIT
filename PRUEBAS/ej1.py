import requests  # Importamos el "teléfono"

# La URL de la API (el "menú" del restaurante)
url = "https://rickandmortyapi.com/api/character/1"

# Hacemos la petición (le pedimos al camarero el plato 1)
respuesta = requests.get(url)

# Convertimos la respuesta en un formato que Python entienda (JSON)
datos = respuesta.json()

# Ahora podemos usar los datos como si fueran un diccionario de Python
print(f"El personaje es: {datos['name']}")
print(f"Especie: {datos['species']}")
print(f"Estado: {datos['status']}")
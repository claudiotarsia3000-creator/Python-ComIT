## Ejercicio 2: Listar Archivos y Directorios
from pathlib import Path 
  
archivo = Path("ejemplo.txt")

archivo.write_text("Este es un archivo de ejemplo.") # Crear un archivo de ejemplo
contenido = archivo.read_text() # Leer el contenido del archivo
print(f"Contenido del archivo: {contenido}")

actual = archivo.read_text() # Leer el contenido del archivo
archivo.write_text("Nuevo contenido del archivo.") # Sobrescribir el contenido del archivo
nuevo_contenido = archivo.read_text() # Leer el nuevo contenido del archivo
print(f"Nuevo contenido del archivo: {nuevo_contenido}")


## Listar todos los archivos y directorios en el directorio actual
for item in Path(".").iterdir():
    if item.is_file():
        print(f"Archivo: {item.name}")
    elif item.is_dir():
        print(f"Directorio: {item.name}")

## Listar solo los archivos con extensión .txt
for f in Path(".").glob("**/*.txt"):
    print(f"Archivo Python: {f.name}")




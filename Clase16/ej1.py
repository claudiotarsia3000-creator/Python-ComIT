from pathlib import Path

archivo = Path("ejemplo.txt")
print(f"Archivo: {archivo}")

actual = Path.cwd()
print(f"Actual: {actual}")

print(archivo.name) # nombre del archivo
print(archivo.suffix) # extensión del archivo
print(archivo.stem) # nombre del archivo sin extensión      
print(archivo.parent) # ruta del directorio donde se encuentra el archivo
print(archivo.exists()) # verifica si el archivo existe
print(archivo.is_file()) # verifica si es un archivo
print(archivo.is_dir()) # verifica si es un directorio  



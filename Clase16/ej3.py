
## Ejercicio 3: Explorar una Carpeta
from pathlib import Path

## Función para explorar una carpeta y mostrar su contenido, resumen de extensiones, cantidad de carpetas y tamaño total
def explorar_carpeta(ruta_str="."):
    carpeta = Path(ruta_str)
## Validar que la ruta exista y sea una carpeta
    if not carpeta.exists():
        print(f"✗ La carpeta '{ruta_str}' no existe")
        return
    if not carpeta.is_dir():
        print(f"✗ '{ruta_str}' no es una carpeta")
        return
## Mostrar el contenido de la carpeta
    print(f"\nContenido de: {carpeta.resolve()}")
    print("-" * 40)

    extensiones = {}
    carpetas = 0
    tamano_total = 0
## Listar archivos y carpetas, calcular resumen de extensiones y tamaño total
    for item in sorted(carpeta.iterdir()):
        if item.is_file():
            tamano = item.stat().st_size
            print(f"{item.name} ({tamano/1024:.1f} KB)")

            ext = item.suffix.lower() if item.suffix else "(sin ext)"
            extensiones[ext] = extensiones.get(ext, 0) + 1
            tamano_total += tamano
        elif item.is_dir():
            print(f"{item.name}/")
            carpetas += 1
## Mostrar resumen de extensiones, cantidad de carpetas y tamaño total
    print("\nResumen:")
    for ext, cantidad in sorted(extensiones.items()):
        print(f"{ext}: {cantidad} archivo(s)")
    print(f"Carpetas: {carpetas}")
    print(f"Tamaño total: {tamano_total/1024:.1f} KB")

explorar_carpeta(".")
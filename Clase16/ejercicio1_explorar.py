# ============================================
# EJERCICIO 1: Explorar directorios
# ============================================
# Crea un script que explore una carpeta y muestre:
# - Lista de archivos y carpetas
# - Conteo por extensión
# - Tamaño total
#
# TIPS:
# - Path.iterdir() para listar
# - .suffix para la extensión
# - .stat().st_size para el tamaño en bytes

from pathlib import Path

def explorar_carpeta(ruta="."):
    carpeta = Path(ruta)
    extensiones = {}
    tamano_total = 0

    print(f"Explorando: {carpeta.resolve()}")
    print("\nArchivos y carpetas:")

    for entrada in carpeta.iterdir():
        tipo = "DIR" if entrada.is_dir() else "FILE"
        print(f"- [{tipo}] {entrada.name}")

        if entrada.is_file():
            ext = entrada.suffix.lower() or "<sin_extension>"
            extensiones[ext] = extensiones.get(ext, 0) + 1
            tamano_total += entrada.stat().st_size

    print("\nConteo por extensión:")
    for ext, cantidad in sorted(extensiones.items()):
        print(f"- {ext}: {cantidad}")

    print(f"\nTamaño total: {tamano_total} bytes")

explorar_carpeta(".")

# Procesador de CSV Manual

def procesar_csv(nombre_archivo):

    """Procesa CSV manejando todos los errores posibles."""
    datos_limpios = []
    errores = []
    try:
        with open(nombre_archivo, "r") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        return [], [f"Archivo '{nombre_archivo}' no encontrado"]
    
    # Primera linea es encabezado
    if len(lineas) < 2:
        return [], ["Archivo vacio o sin datos"]
    encabezados = lineas[0].strip().split(",")
    for i, linea in enumerate(lineas[1:], start=2):
        try:
            valores = linea.strip().split(",")
            if len(valores) != len(encabezados):
                errores.append(f"Linea {i}: columnas incorrectas")
                continue
            registro = {}
            for j, encabezado in enumerate(encabezados):
                valor = valores[j]

                # Intentar convertir a numero si es posible
                try:
                    if "." in valor:
                        registro[encabezado] = float(valor)
                    else:
                        registro[encabezado] = int(valor)
                except ValueError:
                    registro[encabezado] = valor
            datos_limpios.append(registro)
        except IndexError:
            errores.append(f"Linea {i}: error de indice")
    return datos_limpios, errores

# Prueba
datos, errores = procesar_csv("productos.csv")
print("Datos:", datos)
print("Errores:", errores)
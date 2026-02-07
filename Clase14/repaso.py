"""
EJERCICIO DE REPASO: REGISTRO DE NOTAS
Tiempo estimado: 5-10 minutos

Vas a escribir código para clasificar estudiantes
en aprobados y reprobados según su nota.
La nota mínima para aprobar es 70.
"""

# ============================================================
# DATOS - No modificar
# ============================================================

estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 60},
    {"nombre": "María", "nota": 92},
    {"nombre": "Carlos", "nota": 45},
    {"nombre": "Sofía", "nota": 70}
]

# ============================================================
# TAREA 1: Definir la nota mínima como constante
# ============================================================

NOTA_MINIMA = 70


# ============================================================
# TAREA 2: Crear la función evaluar_estudiantes
# ============================================================



def evaluar_estudiantes(lista_estudiantes):
    """
    Clasifica estudiantes en aprobados y reprobados.
    """
    aprobados = []
    reprobados = []
    
    for estudiante in lista_estudiantes:
        if estudiante["nota"] >= NOTA_MINIMA:
            aprobados.append(estudiante["nombre"])
        else:
            reprobados.append(estudiante["nombre"])
    
    return aprobados, reprobados


# ============================================================
# TAREA 3: Llamar la función e imprimir resultados
# ============================================================

aprobados, reprobados = evaluar_estudiantes(estudiantes)
print(f"Aprobados: {', '.join(aprobados)}")
print(f"Reprobados: {', '.join(reprobados)}")


# ============================================================
# PRUEBAS (No modificar - solo ejecutar)
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("                PRUEBAS DEL EJERCICIO")
    print("=" * 50)
    print()

    aprobados, reprobados = evaluar_estudiantes(estudiantes)

    assert aprobados == ["Ana", "María", "Sofía"], f"Aprobados incorrecto: {aprobados}"
    print("    ✓ Aprobados correctos *****")

    assert reprobados == ["Luis", "Carlos"], f"Reprobados incorrecto: {reprobados}"
    print("    ✓ Reprobados correctos *****")

    assert NOTA_MINIMA == 70, "NOTA_MINIMA debe ser 70"
    print("    ✓ Constante correcta *****")

    print()
    print("=" * 50)
    print("            ✓ TODAS LAS PRUEBAS PASARON")
    print("=" * 50)
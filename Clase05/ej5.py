# Validación Profesional

try: 
    # Pedimos la nota (esto puede fallar si escriben letras)
    nota = float(input('¿Cuál es su nota?: '))

    # El bloque IF debe estar DENTRO del try para que se ejecute solo si la nota es válida
    if nota >= 90:
        print('Su Clasificación es: A')
    elif nota >= 80:
        print('Su Clasificación es: B')
    elif nota >= 60:
        print('Su Clasificación es: C')
    elif nota >= 20:
        print('Su Clasificación es: D')
    else:
        print('Su Clasificación es: F')

# Aquí es donde atrapamos el error si el usuario no ingresa un número
except ValueError:
    print("❌ ERROR: Debes ingresar un número válido (ejemplo: 8.5).")

    
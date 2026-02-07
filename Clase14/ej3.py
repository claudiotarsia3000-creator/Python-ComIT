# Calculadora Robusta


def calculadora():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print(f"El resultado de la suma es: {num1 + num2}")
        elif opcion == '2':
            print(f"El resultado de la resta es: {num1 - num2}")
        elif opcion == '3':
            print(f"El resultado de la multiplicación es: {num1 * num2}")
        elif opcion == '4':
            if num2 != 0:
                print(f"El resultado de la división es: {num1 / num2}")
            else:
                print("Error: No se puede dividir por cero.")
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

calculadora()
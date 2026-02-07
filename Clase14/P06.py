# Mini Agenda

def mini_agenda():
    contactos = {}
    def pedir_opcion():
        while True:
            try:
                return int(input("Opcion: "))
            except ValueError:
                print("Escribe un numero")
    while True:
        print("\n--- AGENDA ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar todos")
        print("0. Salir")
        opcion = pedir_opcion()
        if opcion == 0:
            break
        elif opcion == 1:
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            contactos[nombre] = telefono
            print("Contacto agregado!")
        elif opcion == 2:
            nombre = input("Buscar nombre: ")
            try:
                print(f"Telefono: {contactos[nombre]}")
            except KeyError:
                print("Contacto no encontrado")
        elif opcion == 3:
            if contactos:
                for n, t in contactos.items():
                    print(f"  {n}: {t}")
            else:
                print("Agenda vacia")
mini_agenda()
# Sistema de Notas Robusto

import json
class SistemaNotas:
    def __init__(self, archivo="notas.json"):
        self.archivo = archivo
        self.notas = self.cargar()
    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Primera vez. Creando archivo nuevo.")
            return []
        except json.JSONDecodeError:
            print("Archivo corrupto. Iniciando vacio.")
            return []
    def guardar(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump(self.notas, f, indent=2)
        except PermissionError:
            print("Error: sin permisos para guardar")
    def pedir_nota(self):
        while True:
            try:
                nota = float(input("Nota (0-100): "))
                if 0 <= nota <= 100:
                    return nota
                print("Debe estar entre 0 y 100")
            except ValueError:
                print("Escribe un numero valido")
    def agregar(self):
        nombre = input("Nombre del estudiante: ")
        nota = self.pedir_nota()
        self.notas.append({"nombre": nombre, "nota": nota})
        self.guardar()
        print("Nota agregada!")
    def promedio(self):
        if not self.notas:
            print("No hay notas")
            return
        total = sum(n["nota"] for n in self.notas)
        prom = total / len(self.notas)
        print(f"Promedio: {prom:.2f}")
    def listar(self):
        if not self.notas:
            print("No hay notas")
            return
        for n in self.notas:
            print(f"  {n['nombre']}: {n['nota']}")
    def menu(self):
        while True:
            print("\n--- SISTEMA DE NOTAS ---")
            print("1. Agregar nota")
            print("2. Ver promedio")
            print("3. Listar notas")
            print("0. Salir")
            try:
                opcion = int(input("Opcion: "))
            except ValueError:
                print("Escribe un numero")
                continue
            if opcion == 0:
                break
            elif opcion == 1:
                self.agregar()
            elif opcion == 2:
                self.promedio()
            elif opcion == 3:
                self.listar()
                
# Ejecutar
sistema = SistemaNotas()
sistema.menu()
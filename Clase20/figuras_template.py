"""
Clase 20 - Herencia: EJERCICIO 2 — Template para alumnos
=========================================================
Archivo: ejercicio2_template.py

Instrucciones:
- Completa las clases siguiendo los comentarios # TODO:
- Figura es la clase PADRE
- Rectangulo y Circulo son clases HIJAS
- Usa super().__init__() y super().describir()
- Usa import math para math.pi
"""

import math


# ============================================================
# Clase padre: Figura
# ============================================================

class Figura:
    def __init__(self, color):
        # TODO: Guardar color como atributo
        self.color = color

    def calcular_area(self):
        # TODO: Retornar 0 (este es el método base)
        return 0 

    def describir(self):
        # TODO: Imprimir "Soy una figura de color [color]"
        print(f"Soy una figura de color {self.color}")

# ============================================================
# Clase hija: Rectangulo
# Hereda de Figura y agrega: ancho, alto
# ============================================================

class Rectangulo(Figura):  # TODO: Agregar la herencia de Figura
    def __init__(self, color, ancho, alto):
        # TODO: Llamar al __init__ del padre con super()
        super().__init__(color)
        # TODO: Guardar ancho y alto como atributos propios
        self.ancho = ancho
        self.alto = alto 

    def calcular_area(self):
        # TODO: Retornar ancho * alto
        return self.ancho * self.alto
 
    def describir(self):
        # TODO: Llamar a super().describir() primero
        super().describir()
        # TODO: Imprimir "Soy un rectángulo de [ancho]x[alto]"
        print(f"Soy un rectángulo de {self.ancho} X {self.alto}")
        # TODO: Imprimir "Mi área es [calcular_area()]"
        print(f"Mi área es {self.calcular_area()}")


# ============================================================
# Clase hija: Circulo
# Hereda de Figura y agrega: radio
# ============================================================

class Circulo(Figura):  # TODO: Agregar la herencia de Figura
    def __init__(self, color, radio):
        # TODO: Llamar al __init__ del padre con super()
        super().__init__(color)
        # TODO: Guardar radio como atributo propio
        self.radio = radio

    def calcular_area(self):
        # TODO: Retornar math.pi * radio ** 2
        return math.pi * self.radio **2
        
    def describir(self):
        # TODO: Llamar a super().describir() primero
        super().describir()
        # TODO: Imprimir "Soy un círculo de radio [radio]"
        print(f"Soy un círculo de radio {self.radio}")
        # TODO: Imprimir "Mi área es [calcular_area():.2f]"
        print(f"Mi área es {self.calcular_area()}")


# ============================================================
# Pruebas — NO modificar esta sección
# Si tu código es correcto, esto debería funcionar sin errores
# ============================================================

if __name__ == "__main__":

    print("Probando Rectángulo...")
    rect = Rectangulo("azul", 10, 5)
    rect.describir()
    # Esperado:
    #   Soy una figura de color azul
    #   Soy un rectángulo de 10x5
    #   Mi área es 50

    print()

    print("Probando Círculo...")
    circ = Circulo("rojo", 7)
    circ.describir()
    # Esperado:
    #   Soy una figura de color rojo
    #   Soy un círculo de radio 7
    #   Mi área es 153.94

    print()

    print("Verificando herencia...")
    print(f"Rectangulo es Figura: {isinstance(rect, Figura)}")  # True
    print(f"Circulo es Figura: {isinstance(circ, Figura)}")     # True

    print()
    print(f"Área rectángulo: {rect.calcular_area()}")     # 50
    print(f"Área círculo: {circ.calcular_area():.2f}")    # 153.94

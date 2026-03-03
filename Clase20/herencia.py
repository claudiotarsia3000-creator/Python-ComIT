class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola! mi nombre es {self.nombre}")
        print(f"Tengo {self.edad} años.")
        print("¡Encantado de conocerte!")
    
    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tienes {self.edad} años."
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.materias = []

    def estudiar(self, materia):
        print(f"{self.nombre}: Inscrito y cursando las siguiente materia: {materia}.")

    def inscribir_materia(self, materia):
        self.materias.append(materia)
        print(f"{self.nombre} inscrito en {materia}.")

class Profesor(Persona):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.cursos = []

    def enseñar(self, curso):
        print(f"{self.nombre} esta enseñando {curso}.")

    def asignar_curso(self, curso):
        self.cursos.append(curso)
        print(f"{self.nombre} asignado a {curso}.")

# Ejemplo de uso
ana = Estudiante("Ana", 20, "Ingeniería Informática")
carlos = Profesor("Carlos", 45, "Matemáticas")
claudio = Estudiante("Claudio", 45, "AI")

#metodos de la clase Persona
ana.saludar()
carlos.saludar()
claudio.saludar()

#metodos propios
ana.estudiar("Programación")
carlos.enseñar("Álgebra")
claudio.estudiar("AI")
ana.cumplir_anios()
claudio.inscribir_materia("Taller de programacion")
ana.estudiar("Algebra")
carlos.asignar_curso("Fisica")
claudio.estudiar("THP")


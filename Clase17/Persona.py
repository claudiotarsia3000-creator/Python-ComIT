# class Persona:
#     pass

# persona1 = Persona()
# persona2 = Persona()    

# print(type(persona1))
# print(persona1 == persona2)   

# persona3 = Persona()
# persona3.nombre = "Ana"
# persona3.edad = 30
# print(persona3.nombre)
# print(persona3.edad)        

# p1 = Persona()
# p1.nombre = "Juan"

# p2 = Persona()
# p2.nombre = "Maria"

# print(p1.nombre)
# print(p2.nombre)    


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Juan", 30)
print(persona1.nombre)
print(persona1.edad)

persona2 = Persona("Carlos", 25)
print(persona2) 

 
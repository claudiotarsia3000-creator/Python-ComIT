
"""
titulo :string  
prioridad :alto medio baja
categoria :string 
Invalido > raise ValueError("El título no puede estar vacío.")
Invalido > raise ValueError("La pr    y 5.")
Invalido > raise ValueError("La categoría no puede estar vacía.")       

valido > return diccionario con los datos ingresados
"""

def crear_tarea(titulo, prioridad, categoria):
    if not isinstance(titulo, str) or not len (titulo.strip()) == 0:
        raise ValueError("El título no puede estar vacío.")
    prioridad_validas = ["alta", "media", "baja"]
    if prioridad not in prioridad_validas:
        raise ValueError("La prioridad debe ser 'alta', 'media' o 'baja'.")
    if not isinstance(categoria, str) or not len(categoria.strip()) == 0:
        raise ValueError("La categoría no puede estar vacía.")
    
    return {
        "titulo": titulo.strip(),
        "prioridad": prioridad,
        "categoria": categoria.strip(),
        "completada": False
    }     

print(crear_tarea("Estudiar Python", "alta", "Estudio"))    
print(crear_tarea(" ", "media", "Salud"))





 


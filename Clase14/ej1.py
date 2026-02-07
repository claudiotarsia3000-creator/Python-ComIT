#EXCEPCIONES

try:
    numero = int(input("Escribe un numero: "))
    print (f"El doble es: {numero * 2}")

except ValueError:
    
    print("Eso no es un numero valido")
#Meto todo dentro de un WHILE INFINITO, y lo obligo a que de un NUMERO CORRECTO.
#Si no, sigue pidiendo y pidiendo hasta agotas los intentos. Si se agotan, se sale del programa.
# 


intentos = 3
while intentos > 0:
    try:
        numero = int(input("Escribe un numero: "))
        print (f"Su numero es {numero}")
        break
    except ValueError:
        intentos -= 1
        print(f"Eso no es un numero valido. Te quedan {intentos} intentos.")
else:
    print("Has agotado todos los intentos. Adiós.")
    numero = 0




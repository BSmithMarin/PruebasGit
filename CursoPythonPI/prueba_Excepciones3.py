import math

def EvaluEdad(edad):

    if edad<0:
        raise ZeroDivisionError("No se permiten edades negativas")

    if edad<20:
        return "Eres demasiado joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate"

print(EvaluEdad(20))

def calculaRaiz(numero):

    if numero<0:

        raise ValueError("El numero no opuede ser negativo")

    else:
        return math.sqrt(numero)

op1= int(input("Introduce un numero: "))

try:

    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:

    print(ErrorDeNumeroNegativo)

print("Programa termiando")
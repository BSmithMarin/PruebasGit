import math

print("Programa de calculo de raiz cuadrada")
numero=int(input("introduce un numero: "))
intentos=0

while numero<0:
	print("No se admiten numeros negativos")

	if intentos==2:
		print("demasiados intentos, programa finalizado")
		break;												#fuerza la salida del bucle
	numero=int(input("introduce un numero: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrade de ",numero," es ",solucion)
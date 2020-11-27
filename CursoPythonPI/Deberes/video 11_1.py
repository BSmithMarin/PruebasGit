print("Calculadora de numero mayor endl/ bienvenido")
numero1=(int(input("Introduzca el primer numero: ")))
numero2=(int(input("Introduzca el segundo numero: ")))
def DevuelveMax (n1,n2):
	if n1 > n2:
		print("El primero numero es mayor")
	elif n2>n1:
		print("El segundo numero es mayor")
	else:
		print("Ambos numeros son iguales")


DevuelveMax(numero1, numero2)
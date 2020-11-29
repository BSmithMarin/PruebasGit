print("suma de positivos, nunca negativos")

num=int(input("introduzca numero positivo: "))
suma=num
while num>=0:
	num=int(input("introduzca numero positivo: "))
	if num<0:
		break;
	suma=suma+num
	

print("La suma de todos los numeros es: ",suma)
print("Numero negativo, programa finalizado")
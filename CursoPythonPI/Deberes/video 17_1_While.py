print("Numeros cada vez mayores")
numero=int(input("introduce numero:"))
print("numero inicial: ", numero)
numero_anterior=numero
while numero>=numero_anterior :
	numero=int(input("introduce numero: "))
	print("ultimo numero: ",numero)
	if numero<=numero_anterior:
		break;
	numero_anterior=numero
print("Programam finalizado")


	


for i in ["80","20","30210"]:	#La i toma los valores de la lsita, funciona como un contador
	print(i)

email_usuario=str(input("introduce tu email: "))
contador=0
email=False
for i in email_usuario:  #Si se recorre un STRING en vez de una lista, se reccore caracter a caracter
	print(i, end="")
	if(i=="@" or i=="."):
		contador=contador+1
print(" ")
if contador==2:
	print("Email correcto")
else:
	print("Email incorrecto")

for i in range(1,5): #Coge el PRIMERO pero no El ULTIMO
	print(i)
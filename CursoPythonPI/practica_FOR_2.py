for i in range(5,10):
	print( f"valor de la variable: {i}")

valido=False
email=str(input("Introduce tu email: "))
for i in range((len(email))):		#longitud de la variable string
	if email[i]=="@":
		valido=True
	print(email[i])

if valido==True:
	print("Email correcto")

else:
	print("Email incorrecto")

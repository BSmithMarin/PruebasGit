print("Introduce contraseña sin espacios y de al menos 8 caracteres")

password=str(input("introduzca la contraseña:"))
contador=0
espacios=False
for i in password:
	contador=contador+1
	if i==" ":
		espacios=True
if contador>=8 and espacios==False:
	print("La contraseña es correcta")
else:
	print("La contraseña es incorrecta")
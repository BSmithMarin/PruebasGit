email=str(input("introduzca el email: "))

contador=0
punto=False
for i in email:
	if i=="@":
		contador=contador+1
	if i==".":
		punto=True
if contador==1 and punto==True:
	print("email valido")
else:
	print("email NO valido")


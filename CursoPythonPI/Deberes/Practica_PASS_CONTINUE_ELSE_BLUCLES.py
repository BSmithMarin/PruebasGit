for i in "phyton":
	if i=="h":
		continue;
	print("letra:",i )

nombre="pildoras informaticas"
contador=0
for i in nombre:
	if i==" ":
		continue;
	contador+=1

print(contador)

class Miclase:
	pass #para implementar mas tarde

email=input("Introduce tu email: ")

for i in email:
	if i=="@":
		arroba=True
		break;
else:					#Se ejecuta justo despues de acabar el For, a menos que el bucle termine antes

	arroba=False;		#los cual se logra con e BREAK;

print(arroba);

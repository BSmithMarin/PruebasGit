print("Verificacion de acceso")

edad_usuario=int(input("Intruduce tu edad: "))

if edad_usuario<18:
	print("No puedes acceder a este sitio")
elif edad_usuario>100:
	print("Edad incorrecta")

else:
	print("Puedes acceder")
print("Programa finalizado")


#Segunda parte

print("Dispensador den notas")

nota_alumno=float(input("Introduce tu nota: "))

if nota_alumno<5:
	print("Insuficiente")
elif nota_alumno<6:
	print("Suficiente")
elif nota_alumno<7:
	print("Bien")
elif nota_alumno<9:
	print("Notable")
else:
	print("Sobresaliente")

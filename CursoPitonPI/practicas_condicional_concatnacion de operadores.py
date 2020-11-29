edad=-300

if 0<edad<100:
	print("Edad es correcta")
else:
	print("Edad incorrecta")

spresidente=int(input("salario presidente: "))
print("Salario presidente:",spresidente)

sdirector=int(input("salario director: "))
print("Salario director:",sdirector)

sjefearea=int(input("salario jefe de area: "))
print("Salario presidente:",sjefearea)

sadministrativo=int(input("salario administrativo: "))
print("Salario administrativo:",sadministrativo)

if spresidente>sdirector>sjefearea>sadministrativo:
	print("Los salarios estan bien")
else:
	print("Algo falla")
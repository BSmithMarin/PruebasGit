print("Asignaturas optativas 2019")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
asignatura=input("Escribe la asignatura seleccionada: ")

opcion=asignatura.lower()   #convuerte en minuscula la variable string que lo acompaña
							#Para mayuscula se usa .upper() 


if opcion in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):

	print("Asignatura elegida: ",opcion)
else:

	print("Asignatura no contemplada, intentelo de nuevo")
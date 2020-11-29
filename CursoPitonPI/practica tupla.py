mitupla=("Juan",13,1,1995)

print(mitupla[2])

milista=list(mitupla)		#convertir tupla en lista

print(milista)

print(mitupla)

mitupla2=tuple(milista) 	#convertir lista en tupla

print("Juan" in mitupla)	#revisa si el elemento esta en el conjunto

print(mitupla.count(13))	#cuenta cuantas veces esta el elemento en la tupla

print(len(mitupla2))		#devulve la LONGITUD del conjunto

nombre, dia, mes, agno=mitupla2		#DESEMPAQUETADO DE TUPLA, asigna por oden todos los valores a de una tupla a una serie de variables

print(nombre)
print(agno)
print(dia)
print(mes)

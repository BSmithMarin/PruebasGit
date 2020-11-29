print("Calculo de drecho a beca")
distancia_escuela=int(input("introduce la distancia al centro en KM: "))
print("Distancia escuela: ",distancia_escuela)

nhermanos=int(input("Numero de hermanos: "))
print("Numero de hermanos: ",nhermanos)
rentafamiliar=int(input("Renta familiar el año anterior: "))
print("Renta familiar: ",rentafamiliar)

if distancia_escuela>40 and nhermanos>2 or rentafamiliar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")
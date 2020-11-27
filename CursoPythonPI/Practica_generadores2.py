#def devulve_ciudades(*ciudades):
 #   for elemento in ciudades:
  #      for subElemento in elemento:
   #         yield subElemento

def devulve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas=devulve_ciudades("Madrid","Baecelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
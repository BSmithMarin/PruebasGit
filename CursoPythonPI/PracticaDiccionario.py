
miDiccionario={"Alemania":"Berlin","Francia":"Paris","UK":"Londres","Espagna":"Madrid"}

#Diccionarios guardan valores de dos en dos, Clave:Valor, puden guardar todo tipo de datos, incluso listas, tuplas y otros diccionarios

print(miDiccionario["Francia"])

miDiccionario["Italia"]="Lisboa"	#establecer o modificar valerees dentro del diccionario

print(miDiccionario)

del miDiccionario["UK"]

print(miDiccionario)

miDiccionario2={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}

mitupla=("Espagna","Francia","Reino Unido","Alemania")
midiccionario={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(midiccionario)

#utilizo los datos contenidos en una TUPLA para asignar las claves de un diccionario

print(midiccionario[mitupla[2]])

midiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":(91,92,93,96,97,98)}
print(midiccionario3["Anillos"]) 	#Se mete una tupla en el diccionario

#Meter un diccionario dentro de otro diccionario

midiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":(91,92,93,96,97,98)}}
print(midiccionario4.keys(),"Claves")		#Devulve las claves del diccionario
print(midiccionario4.values())				#Valores del diccionario
print(len(midiccionario4))					#Longitud del diccionario
print(midiccionario4["Anillos"])
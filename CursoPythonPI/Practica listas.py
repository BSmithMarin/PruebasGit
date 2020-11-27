miLista=["Maria","pepe", "marta", "antonio"]

miLista.extend(["sandra","Ana","Lucia"])  #concantena elementos a la lista

miLista.append(5)		#inserta un elemeneto a lista en ultima posicion

miLista.insert(0,True)	#inserta en la posicion deseada un elelemento a la lista

miLista.remove("Ana")	#Elimina el elemento de la lista

miLista.pop()        #Elimina el ultimo elemento de la lista

print(miLista[:])

print(miLista.index("antonio"))		#Indica la posicion dentro de la lista del elemento

print("pepe" in miLista)		#Idica si el elemento buscado se encuentra en la lista o no

miLista2=["Carlos","Marcos"] *3 	#Triplica los elementos de la lista (se imprime 3 veces)

miLista3=miLista+miLista2		#concatena dos listas por el operador suma

print(miLista3[:])

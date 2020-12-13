from io import open

#---------------------Escritura y creación de un archivo de txt------------------------

archivo_texto=open("archivo.txt","w")

frase="Mi primera frase en un archivo externo, glorioso dia \n Para la segunda linea no tengo mas ideas"

archivo_texto.write(frase)

archivo_texto.close() #cerrar en memoria ,no como en Windows

#-------Apertura en modo lectura de un archivo existente, guardado de su contrnido en una varibale------


archivo_texto=open("archivo.txt","r")

#Al pricipio solo se habia abierto en modo escritura
#por lo que no se puede leer y guardar en una variable el contenido del archivo

textoArchivo=archivo_texto.read()

archivo_texto.close() #cerrar en memoria ,no como en Windows

print(textoArchivo)

#---------Guardado del contido del archivo de TXT en un Array, linea a linea-------------+

archivo_texto=open("archivo.txt","r")

textoArchivoArray=archivo_texto.readlines()

archivo_texto.close()

print(textoArchivoArray[1])

#------Añadir contenido a un archivo ya existente-----

archivo_texto=open("archivo.txt","a") #Append

archivo_texto.write("\n siempre es una buena ocasion para apremder Python")

archivo_texto.close()

#-------MAnejo de punteros en archivos de texto--------
'''
Cunado abrimos un archivo de texto el PUNTERO se situa por defecto en la posicion 0
al acabar de leer un archivo se queda situado en el ultimo caracter leido
cuando abrimos un documento con APPEND como parametro tambien se situa en el ultimo carácter 
del archivo, para poder añador contenido al archivo
'''


archivo_texto=open("archivo.txt","r")

print()

archivo_texto.close()


#Importa todos los metodos, variables y clases del archivo FuncionesMatematicas
#Se le cambia el nombre para que sea mas facil e intuitivo al usarse

import FuncionesMatematicas as math

#Con el asterisco se importan todos lo metodos y clases del archivo 
from FuncionesMatematicas import *

# se importan todos los metodos del archivo, pero para usarse se deben usar come metodos
# de una clase, poniendo el nombre del archivo delante "." el metodo que queremos usar
import FuncionesMatematicas

print(math.suma(5,7))
print(suma(5.0,3.0))
print(multiplicar(3,6))

print(FuncionesMatematicas.suma(12.0,80.0))
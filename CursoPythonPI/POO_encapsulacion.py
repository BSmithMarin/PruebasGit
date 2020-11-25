class Coche():

    def __init__(self):

        self.__anchoChasis=120
        self.__largoChasis=250
        self.__ruedas=4 #Se encapsula la variable, no es accesible desde fuera de la clase
        self.__enMarcha=False

    def Arrancar(self,arrancamos):
        print("Arranco")
        self.enMarcha=arrancamos
        if (self.enMarcha):
            chequeo=self.__chequeoInterno()
            if(chequeo):
                return "El Coche esta en marcha"
            else:
                return "El coche NO esta en condiciones de arrancar"
        else:
            return "El coche no se ha arrancado"

    
    def estado(self):
        if(self.__enMarcha):
            return "El coche esta en marcha"
        else:

            return " El coche esta parado"
    
    def __chequeoInterno (self):
        print("Realizando chequeo de componentes")

        self.gasolina=True
        self.aceite=True
        self.puertas=True

        if(self.gasolina and self.puertas and self.aceite):
            return True
        else:
            return False


miCoche=Coche()

miCoche.Arrancar(True)

print(miCoche.estado())

print("----------Aqui creamos el segundo objeto------------")

miCoche2=Coche()

print(miCoche2.estado())

miCoche2.ruedas=5 #Esta variable no tiene nada que ver con las variabel __ruedas
                  #que se encuentra en el constructur de la clase Coche()

print("el coche 2 tiene ",miCoche2.ruedas, "Ruedas")
#print("el coche 2 tiene ",miCoche2.__ruedas," ruedas") 
''' No funciona por que la variable no es accesible desde el exterior'''

print("----------Aqui probamos el encapsulamiento------------")

miCoche2.aceite=True #No permite modificar la variable                       
print(miCoche2.Arrancar(True))

print(miCoche.puertas) #auqnue la variable se encuentre definida ene un metodo
                        # es accesible desde otros lugares, aunque no se jecute el método
                        #aunque esta este ENCAPSULADO, su varibales internas si son accesibles

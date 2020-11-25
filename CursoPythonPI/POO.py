class Coche():

    def __init__(self):

        self.anchoChasis=120
        self.largoChasis=250
        self.__ruedas=4 #Se encapsula la variabel, no es accesible desde fuera de la clase
        self.enMarcha=False

    def Arrancar(self,arrancamos):
        print("Arranco")
        self.enMarcha=arrancamos

    
    def estado(self):
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:

            return " El coche esta parado"

miCoche=Coche()

miCoche.Arrancar(True)

print(miCoche.estado())

print("----------Aqui creamos el segundo objeto------------")

miCoche2=Coche()

print(miCoche2.estado())

miCoche2.ruedas=5 #Esta variable no tiene nada que ver con las variabel __ruedas
                  # que se encuentra en el constructur de la clase Coche()

print("el coche 2 tiene ",miCoche2.ruedas, "Ruedas")
print("el coche 2 tiene ",miCoche2)
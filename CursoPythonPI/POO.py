class Coche():
    anchoChasis=120
    largoChasis=250
    ruedas=4
    enMarcha=False

    def Arrancar(self):
        print("Arranco")
        self.enMarcha=True
    
    def estado(self):
        if(self.enMarcha):
            return "El coche esta en amrcha"
        else:

            return " El coche esta parado"

miCoche=Coche()

#miCoche.Arrancar()

print(miCoche.estado())
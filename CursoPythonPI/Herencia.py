class Vehiculos():

    def __init__(self,marca,modelo):

        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enMarcha=True

    def acelerar(self):

        self.acelera=True
    
    def frenar(self):

        self.frena=True
    
    def estado(self):

        print("Marca: ",self.marca," Modelo: ",self.modelo,"\n en marcha: ",self.enMarcha,
         "Acelera: ",self.acelera," frena: ",self.frena)

class Moto(Vehiculos): #se pasa por parametro la clase de que hereda
    pass

miMoto=Moto("Honda","CRX")

miMoto.estado()



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

class Furgoneta(Vehiculos):

    def carga(self, carga):
        self.cargado=carga
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta NO esta cargada"

class Moto(Vehiculos): #se pasa por parametro la clase de que hereda
    
    hcaballito=""
    
    def caballito(self):
        self.hcaballito="Hago un caballito"

    def estado(self): #Sobreescribimos el valor de la funcion estado de la clase padre
                      #

        print("Marca: ",self.marca," Modelo: ",self.modelo,"\n en marcha: ",self.enMarcha,
         "Acelera: ",self.acelera," frena: ",self.frena, "\nHaciendo caballito: ",self.hcaballito)

class VElectricos():

    def __init__(self):
        self.autonomia=100
    
    def cargaEnergia(self):

        self.cargando=True

miMoto=Moto("Honda","CRX")

miMoto.caballito()

miMoto.estado()

print("----------------Aqui empeiza la clase furgoneta-----------")

miFurgoneta=Furgoneta("Renault","Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(False))


class BicicletaElectrica(Vehiculos,VElectricos): #Se hereda el constructor de la primera clase padre
    pass

miBiciE=BicicletaElectrica("BMX","Eedition")

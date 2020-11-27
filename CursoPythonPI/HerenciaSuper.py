class Persona ():
    def __init__(self,nombre,edad,direccion):

        self.nombre=nombre
        self.edad=edad
        self.direccion=direccion

def descripcion(self):

    print("Nombre: ", self.nombre, "Edad: ",self.edad, "direccion: ",self.direccion)

miPersona=Persona("Alejandro",18,"Holanda")
miPersona.descripcion()
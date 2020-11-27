 #La funcion super() ejecuta el metodo de la clase padre y despues lo añadido en la clase hija
 #La herencia se rige por el principio de sustitucion, por lo que un objeto de la clase hija
 #siempre es rambién un objeto de la clase padre, siempre se es persona antes que empleado


 #la funcion is isinstance(objeto,clase) nos devulve si un objeto pertenece o una clase 
 #lo devulve mediante False o True

class Persona ():

    def __init__(self,nombre,edad,direccion):

        self.nombre=nombre
        self.edad=edad
        self.direccion=direccion

    def descripcion(self):

        print("Nombre: ", self.nombre, "Edad: ",self.edad, "direccion: ",self.direccion)

miPersona=Persona("Alejandro",18,"Holanda")
miPersona.descripcion()

print("-----------Empieza el empleado------------------------")

class Empleado(Persona):

    def __init__(self,salario,antiguedad,nombre,edad,residencia):

       #La funcion super() ejecuta el metodo de la clase padre y despues lo añadido en la clase hija
       
        super().__init__(nombre,edad,residencia)

        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print("Sueldo: ",self.salario,"Antiguedad; ",self.antiguedad," Años")

miEmpleado=Empleado(55000,5,"Brahyan",23,"Portugal")

miEmpleado.descripcion()

print(isinstance(miEmpleado,Empleado))
print(isinstance(miEmpleado,Persona))
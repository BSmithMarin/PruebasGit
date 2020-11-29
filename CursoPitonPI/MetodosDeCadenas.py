nombreUsuario=input("Introduce tu User name: ")

print("el nombre es: ",nombreUsuario)

print("el nombre es: ",nombreUsuario.upper())
print("el nombre es: ",nombreUsuario.lower())
print("el nombre es: ",nombreUsuario.capitalize())

edad=input("Introduce tu edad: ")

print(edad.isdigit())

if edad.isdigit():
    int(edad)

    if(edad>18):

        print("Puedes pasar")
    else:

        print("No puedes pasar ")
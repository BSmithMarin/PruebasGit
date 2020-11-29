def divide():
    try:
        num1=(float(input("Introduce numero 1: ")))
        num2=(float(input("Introduce numero 2: ")))

        print("LA division es: "+str(num1/num2))
    except ValueError:
        print("Tipo de dato erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except:
        print("Ha ocurrido un error")

    finally:
        print("calculo finalizado")
#EL finally sirve para que un bloque de codigo se ejecute si o si
#Auqnue ocurra un error durante la ejecucuion, sirve ppor ejemplo, para
#que siempre se cierre la conexion con una base de datos al acabar un programa
#pase lo que pase antes.

divide()
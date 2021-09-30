#1.	Solicitar al usuario que ingrese su dirección de correo electrónico. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
nombre=input("Dime tu nombre: ")

def Direccion_correo(cuenta):
    f=cuenta.count("@")
    if f==1:
        return True
    return False
cuenta= input("Ingrese su correo electronico: ")
if Direccion_correo(cuenta):
    print(nombre +" tu dirección de correo valida,", "hasta luego.")
else:
    print(nombre+" tu dirección de correo es invalida,", "por favor intenta de nuevo.")
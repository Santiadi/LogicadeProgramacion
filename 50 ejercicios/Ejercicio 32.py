#32.	Escribe un algoritmo o el respectivo diagrama de flujo que permita determinar si un año dado es o no bisiesto.
a=int(input("Digíte el año: "))
if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
 print("El año "+str(a)+" Si es bisiesto ")
else:
 print("El año "+str(a)+" No es bisiesto ")
#29.	Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y determine el mayor y el menor de ellos.
a=int(input("Dig�te un n�mero: "))
b=int(input("Dig�te otro n�mero: "))
c=int(input("Dig�te otro n�mero: "))
if(a > b and a > c):
 print("El n�mero mayor es: " + str(a))
else:
 if(b > a and b > c):
  print("El n�mero mayor es: " + str(b))
 else:
  print("El n�mero mayor es: " + str(c))
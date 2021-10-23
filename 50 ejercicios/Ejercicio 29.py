#29.	Escribe un algoritmo o el respectivo diagrama de flujo que lea tres nÃºmeros y determine el mayor y el menor de ellos.
a=int(input("Digíte un número: "))
b=int(input("Digíte otro número: "))
c=int(input("Digíte otro número: "))
if(a > b and a > c):
 print("El número mayor es: " + str(a))
else:
 if(b > a and b > c):
  print("El número mayor es: " + str(b))
 else:
  print("El número mayor es: " + str(c))
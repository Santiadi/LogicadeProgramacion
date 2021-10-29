#52.	Construye un algoritmo y el respectivo diagrama de flujo que permita leer una cantidad variable de números y nos indique cuantos fueron mayores a 100 y cuántos menores a 100.
a=0
b=0
n = int(input("Digí­ta la cantidad de números que desee: "))
for i in range(n):
    n1 = int(input("Digíte un número: "))
    if n1 >= 100:
      a += 1
    else:
        b += 1
print("Estos son los números mayores a 100: ", a, " y estos son los menores a 100: ", b)
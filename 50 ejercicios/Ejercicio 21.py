#21.	Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y determine si es par o impar.
numero = int(input("Digíte un número para saber si es impar o par: "))
if (numero % 2) == 0:
  print(numero, " es par")
else:
  print(numero, " es impar")
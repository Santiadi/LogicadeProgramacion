#48.	Escribe un algoritmo o el respectivo diagrama de flujo que lea 10 nÃºmeros y calcule su suma y su promedio
suma = 0
print("Digí­te 10 números: ")
for i in range(10):
    numero = int(input())
    suma = suma+numero
print("La suma es: ", suma)
print("La división es: ", suma/10)
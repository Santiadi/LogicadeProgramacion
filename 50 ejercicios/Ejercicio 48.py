#48.	Escribe un algoritmo o el respectivo diagrama de flujo que lea 10 números y calcule su suma y su promedio
suma = 0
print("Dig�te 10 n�meros: ")
for i in range(10):
    numero = int(input())
    suma = suma+numero
print("La suma es: ", suma)
print("La divisi�n es: ", suma/10)
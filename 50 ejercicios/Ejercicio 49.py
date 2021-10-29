#49.	Escribe un algoritmo o el respectivo diagrama de flujo que lea n nÃºmeros y calcule su suma y su promedio
suma=0
n=int(input("Digí­ta la cantidad de números que desee: "))
for i in range(n):
    numero=int(input())
    suma=suma+numero
print("La suma es: ", suma)
print("La división es: ", suma/n)
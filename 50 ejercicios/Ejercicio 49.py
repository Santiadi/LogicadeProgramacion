#49.	Escribe un algoritmo o el respectivo diagrama de flujo que lea n números y calcule su suma y su promedio
suma=0
n=int(input("Dig�ta la cantidad de n�meros que desee: "))
for i in range(n):
    numero=int(input())
    suma=suma+numero
print("La suma es: ", suma)
print("La divisi�n es: ", suma/n)
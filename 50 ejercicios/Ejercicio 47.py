#47.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la suma de los números naturales contenidos entre dos números n y m (verificar que m>n)
m=int(input("Digíte un número: "))
n=int(input("Digíte un número: "))
suma=0
while m>n:
    for i in range (n,m):
        suma=suma+i
        print(suma)
    break
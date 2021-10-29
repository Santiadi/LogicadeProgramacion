#46.	Escribe un algoritmo o el respectivo diagrama de flujo que imprima los números naturales contenidos entre dos números n y m (verificar que m>n)
m=int(input("Digíte un número: "))
n=int(input("Digíte un número: "))
while m>n:
    for i in range (n,m):
        print(i)
    break
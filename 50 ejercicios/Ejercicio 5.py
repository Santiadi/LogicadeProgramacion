#5.	Escribe un algoritmo o el respectivo diagrama de flujo que lea un número decimal e imprima su parte entera y su parte decimal por aparte.
numero=float(input("Dame un número decimal: "))
n=numero//1
numero=n%1
n=int(n)
print("parte entera: ",n)
print("Parte decimal: ",numero)
#23. Escribe un algoritmo o el respectivo diagrama de flujo que lea un número e indique si este es par-positivo, par-negativo, impar-positivo o impar-negativo.
n=int(input("Digíte un número: " ))
if n%2==0:
    while n>=0:
        print(n,"es par-positivo")
        break
    else:
        print(n,"es par-negativo")
elif n>=0:
    print(n,"es impar-positivo")
else:
    print(n,"es impar-negarivo")
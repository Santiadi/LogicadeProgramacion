#51.	Construye un algoritmo y el respectivo diagrama de flujo que le solicite al usuario un número entero positivo, si el usuario digita un valor no permito, le debe volver a pedir el número. Una vez ingrese un valor válido deberá imprimir dicho valor.
num=int(input("Digíte un número: "))
while num<0:
    num=int(input("Digíte de nuevo el número: "))
else:
    print(num)
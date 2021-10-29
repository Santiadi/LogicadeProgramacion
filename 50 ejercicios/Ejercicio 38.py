#38.	Escribe un algoritmo o el respectivo diagrama de flujo que, dados dos números, verifique si ambos están entre 0 y 5 o retorne false sino es cierto. Por ejemplo 1 y 2 ---> true ; 1 y 8 ---> false
n = float(input("Digíte un número: "))
n1 = float(input("Digíte otro número: "))
if 0 <= n <= 5 and 0 <= n1 <= 5:
    print("Los números estan entre 0 y 5.")
elif 0 <= n <=5:
        print("El primer número esta entre 0 y 5.")   
elif  0 <= n1 <= 5:
        print("El segundo número esta entre 0 y 5.")
else:
        print("Ninguno de los dos números estan entre 0 y 5.")
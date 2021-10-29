#36.	Escribe un algoritmo o el respectivo diagrama de flujo que dado un número menor a un 100.000 determine la cantidad de dígitos que tiene. Por ejemplo 1093 tiene 4 dígitos.
num = input("Digíte un número: ")

num1 = num.split(".")
num1 = int("".join(num1))

if num1 < 100000:
    print(num, "tiene", len(str(num1)),"digitos.")

else:
    print("El número ingresado es mayor que 100.000.")
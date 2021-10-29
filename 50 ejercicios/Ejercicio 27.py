#27.	Escribe un algoritmo o el respectivo diagrama de flujo que lea dos números y determine el mayor de ellos.
num1,num2=int(input("Digíte un número: ")),int(input("Digíte otro número: "))
if num1==num2:
    print("Los número son iguales")
elif num1<num2:
    print("El primer número es menor")
elif num1>num2:
    print("El primer número es mayor")
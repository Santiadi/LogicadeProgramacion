#10.	Escribe un algoritmo o el respectivo diagrama de flujo que intercambie el valor de dos variables e imprima los valores antes y después del intercambio. Por ejemplo, si a = 1 y b = 3, al intercambiar sus valores serán a = 3 y b = 1 (Consejo: usar variable auxiliar).
a=int(input("Ingrese un número entero: "))
b=int(input("Ingrese otro número entero: "))
print("Antes del intercambio: ", a,b)
aux=a
a=b
b=aux
print("Intercambio: ",a,b)
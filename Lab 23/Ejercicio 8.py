#Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.
def prim(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def frecuencia(n, dig):
    c = 0
    while n != 0:
        Digito = n % 10
        if Digito == dig:
            c += 1
        n = n // 10
    return c
def factorial(n):
    f = 1
    if n != 0:
        for i in range(1, n + 1):
            f = f * i
    return f
def sumaDig(n):
    sum = 0
    while n != 0:
        dig = n % 10
        sum = sum + dig
        n = n // 10
    return sum
mayor = 0
n = int(input("Número primo: "))
while prim(n):
    print("Suma de los dígitos:", sumaDig(n))
    dig = int(input("Dígito: "))
    print("El", dig, "aparece", frecuencia(n, dig), "veces")
    if n > mayor:
        mayor = n
    n = int(input("Número primo: "))
print("Factorial de", mayor, ":", factorial(mayor))
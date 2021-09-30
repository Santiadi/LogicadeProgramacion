#7.Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.
def DigSu(numero):
    sum = 0
    while numero != 0:
        digito = numero % 10
        sum = sum + digito
        numero = numero // 10
    return sum
c = 0
m = -1
nume = int(input("Número positivo: "))
while nume >= 0:
    sum = DigSu(nume)
    if sum > m:
        m = sum
        mayorsuma = nume
    if sum < 10:
        c += 1
    nume = int(input("Número positivo: "))
print("Sumatoria de dígitos de", mayorsuma, ":", m)
print("Cantidad con sumatoria menor a 10:", c)
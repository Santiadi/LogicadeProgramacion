#30.	Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y determine si la suma del primero y el segundo es mayor o menor que el tercero.
num1,num2,num3=int(input("Digíte un número")),int(input("Digíte un número")),int(input("Digíte un número"))
suma=num1+num2
if suma>num3:
    print(suma,"Es mayor a",num3)
else:
    print(num3,"Es mayor a",suma)
#54.	Construye un algoritmo y el respectivo diagrama de flujo que permita leer sólo números positivos hasta reunir 10 números pares o veinte veces el número 5. Indicar luego la totalidad de números leídos, la cantidad de pares, de impares y la cantidad de números 5.
a=0
b=0
c=0

while a!=10:
    num=int(input("Digíte un número: "))
    if num<0:
        print("Solo se pueden ingresar numeros positivos")
        exit()
    elif num%2==0 and num>0:
        a+=1
    elif num==5:
        b+=1
        c+=1
        if b==20:
            break
    else:
        c+=1
print("la cantidad de numeros introducidos fue:",a+b+c," Donde:",a,"fueron numeros pares",b,"fueron numeros '5'",c,"fueron numeros impares")
#20.	Escribe un algoritmo o el respectivo diagrama de flujo que, dada un numero de 4 cifras, reordene sus dígitos de manera inversa. Por ejemplo 3245 ---> 5423
a=int(input("Digíte un número de 4 cifras: "))
cifra_4=a%10
cifra_3=int((a%100)/10)
cifra_2=int((a%1000)/100)
cifra_1=int((a-(a%1000))/1000)
print(str(cifra_4)+str(cifra_3)+str(cifra_2)+str(cifra_1))
#3.  números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.  este no es.
def sumDig(n):
    sum=0
    while n!=0:
        dig=n%10
        sum=sum+dig
        numero=n//10
    return sum
sumTo=0
num=int(input("Escribe un número para procesar,si quiere finalizar ingresa un 0: "))
while num!=0:
    print("Suma:",sumDig(num))
    sumTo=sumTo+num
    num=int(input("Escribe un número para procesar,si quiere finalizar ingresa un 0: "))
print("Sumatoria:", sumTo)
print("Dígitos:", sumDig(sumTo))
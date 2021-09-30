#2.	Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).
def DigSuma(numero):
    sum=0
    for a in range(numero):
        dig=numero%10
        sum=sum+dig
        numero=numero//10
    return sum
num=int(input("Escribe un número para procesar, si quiere finalizar ingresa un 0: "))
while num!=0:
    print("suma:", DigSuma(num))
    num=int(input("Escribe un número para procesar, si quiere finalizar ingresa un 0: "))
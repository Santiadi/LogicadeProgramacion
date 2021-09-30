#4. Solicitar al usuario que ingrese un número entero e informarle si es primo o no, utiliza en el código una función booleana que lo decida.
def Número_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
def primo():
    num = int(input("Escribe un número: "))
    result = Número_primo(num)

    if result is True:
        print("El número es primo")
    else:
        print("El número no es primo")
primo()
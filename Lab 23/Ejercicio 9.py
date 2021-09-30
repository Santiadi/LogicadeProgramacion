#9.Escribir una función que, dado un número de cédula de ciudadanía, retorne True si el número es válido y False si no lo es. Consulta cuál es la longitud válida para cédula en Colombia.
y=2
def f(num):
   cantidad=0
   while num!=0:
       Dig=num%10
       cantidad+=1
       num=num//10
   return cantidad
while y==2:
    hi=input("""que desea ingresar:
    1.Cedula de ciudadania
    2.Tarjeta de identidad
    """)
    num=int(input("ingrese el numero: "))
    if f(num)>10:
        print("El número es invalido")
    elif f(num)==10:
        print("Número es valido")
    elif f(num)<10:
        print("El número es invalido")
    else:
        print("Intenta de nuevo")
    break
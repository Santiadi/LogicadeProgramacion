#6. Escribir un programa que pida números al usuario, mostrar la factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
def f(n):
   f=1
   if n!=0:
       for i in range(1,n+1):
           f=f*i
   return f
c=0
num=int(input("ingrese un Número, si quiere terminar ingrese un -1: "))
while num!=-1:
    print("Factorial:", f(num))
    c+=1
    num=int(input("ingrese un Número, si quiere terminar ingrese un -1: "))
print("Se leyeron",c,"números ingresados")
#25.	Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y si este es mayor o igual a 10 devuelva el triple de este, de lo contrario la cuarta parte de este.
num=int(input("Digíte un número: "))
while num>=10:
    triple=num*3
    print("Esté es el triple: ", triple)
    break
while num<10:
    cuarta=num*4
    print("Esté es el cuadruple: ", cuarta)
    break
#33.	Escribe un algoritmo o el respectivo diagrama de flujo que permita resolver una ecuación cuadrática de tipo ax2 + bx + c (tenga en cuenta las todas las raíces, tanto las reales como las complejas).
a=int(input("Digíte un número: "))
b=int(input("Digíte un número: "))
c=int(input("Digíte un número: "))
if((b**2)-4*a*c)<0:
    print("Resultado de la ecuasión es con número complejos")
else:
    n1=(-b+str(b**2-(4*a*c)))/(2*a)
    n2=(-b-str(b**2-(4*a*c)))/(2*a)
    print("Las soluciones son: ",n1,n2)
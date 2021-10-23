#11.	Escribe un algoritmo o el respectivo diagrama de flujo que determine el tiempo de caída de un objeto que se suelta desde una altura h.
h=float(input("Digíte la altura para evaluar el tiempo de caída: "))
t=((2*h)/9.81)**0.5
print("Esté es el tiempo de caída del objeto:",t, "s")
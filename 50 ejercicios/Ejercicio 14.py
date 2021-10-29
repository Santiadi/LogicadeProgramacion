#14.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la energía (en Julios) de un objeto si se conoce la masa de un objeto (en kg) y la velocidad de la luz (en m/s).
m,v=float(input("Digíta la masa: ")), float(input("Digíta la velocidad: "))
e=1/2*m*v**2
print("La energía es:", e,"J")
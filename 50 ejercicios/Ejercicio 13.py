#13.	Escribe un algoritmo o el respectivo diagrama de flujo que determine la velocidad final de un objeto luego de un tiempo, si se sabe que va en línea recta y además se conoce su aceleración.
vi,t=float(input("Digíta la velocidad incial: ")),float(input("Digíte el tiempo: "))
vf=(vi+9.81*t)**0.5
print("Está es la velocidad final: ", vi, "m/s")
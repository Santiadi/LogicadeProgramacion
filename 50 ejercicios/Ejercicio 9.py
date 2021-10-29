#9.	Escribe un algoritmo o el respectivo diagrama de flujo que dados tres números calcule el promedio de dichos números.
print("Dame 3 notas de tú colegio para calcular tu promedio:")
n1,n2,n3=float(input("Digita tu primera nota: ")),float(input("Digita tu segunda nota: ")),float(input("Digita tu tercera nota: "))
n1=n1+n2+n3
nt=(n1/3)**0.5
print("Este es tu promedio: ", nt)
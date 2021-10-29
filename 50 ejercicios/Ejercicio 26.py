#26.	Escribe un algoritmo o el respectivo diagrama de flujo que lea las cinco notas obtenidas por un estudiante y calcule su nota final, sabiendo que las cada nota tiene el siguiente valor: n1 (15%), n2 (20%), n3 (15%), n4 (30%), n5 (20%). Si la nota obtenida es menor a 2,0 deberá indicarle al estudiante que no puede habilitar, si la nota obtenida es menor a 3 deberá indicar que reprobó, si la nota es mayor o igual a 3 deberá indicar que aprobó y si es mayor a 4,5 extenderá un mensaje de felicitación al estudiante.#
n1=float(input("Digíte tú primera nota que es el 15%: "))
n2=float(input("Digíte tú segunda nota que es el 20%: "))
n3=float(input("Digíte tú tercera nota que es el 15%: "))
n4=float(input("Digíte tú cuarta nota que es el 30%: "))
n5=float(input("Digíte tú quinta nota que es el 20%: "))
n1=n1*0.15
n2=n2*0.20
n3=n3*0.15
n4=n4*0.30
n5=n5*0.20
nt=n1+n2+n3+n4+n5
while nt<2.0:
    print("No puedes habilitar")
    break
while nt<3.0:
    print("Reprobaste :(")
while nt>=3.01:
    print("Aprobaste :)")
    break
while nt>4.5:
    print("Fecilicidades por tu nota :D")
    break
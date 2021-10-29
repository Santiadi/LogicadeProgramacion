#35.	Escribe un algoritmo o el respectivo diagrama de flujo que dado un número entre 0 y 10, imprima el nombre del número. Ejemplo: 1 ---> UNO
num=int(input("Digíte un número entre el 1 al 10: "))
if num<0 and num>10:
    print("El número es invalido")
elif num==1:
    print(num,"= UNO")
elif num==2:
    print(num,"= Dos")
elif num==3:
    print(num,"= Tres")
elif num==4:
    print(num,"= Cuatro")
elif num==5:
    print(num,"= Cinco")
elif num==6:
    print(num,"= Seis")
elif num==7:
    print(num,"= Siete")
elif num==8:
    print(num,"= Ocho")
elif num==9:
    print(num,"= Nueve")
else:
    print(num,"= Diez")
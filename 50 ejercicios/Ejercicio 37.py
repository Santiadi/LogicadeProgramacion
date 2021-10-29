#37.	Escribe un algoritmo o el respectivo diagrama de flujo que dados 3 números, determine si los números se están incrementando, disminuyendo o ninguno de lo anterior de acuerdo con el orden de digitación. Por ejemplo: 1 , 4, 19 --> está incrementando  ;  33, 10 ,1 --> está disminuyendo;   3 , 18 , 10 --> Ni se incrementa ni se disminuyendo
n = input("Digíte 3 números separados: ")
n = n.split(" ")
if float(n[0]) < float(n[1]) and float(n[1]) < float(n [2]):
    print("Los números se incrementan")
elif float(n[0]) > float(n[1]) and float(n[1]) > float(n[2]):
    print("Los números disminuyen")
else:
    print("Intente de nuevo")
#19.	Escribe un algoritmo o el respectivo diagrama de flujo que, dada una cantidad de dinero, determine la menor cantidad de billetes de cada denominación que se puede entregar.
m=int(input("Digíte la cantidad en pesos COP: "))
billete_100k=(m%100000)/100000
m=m%100000
billete_50k=(m%50000)/50000
m=m%50000
billete_20k=(m%20000)/20000
m=m%20000
billete_10k=(m%10000)/10000
m=m%10000
billete_5k=(m%5000)/5000
m=m%5000
billete_2k=(m%2000)/2000
m=m%2000
billete_1k=(m%1000)/1000
m=m%1000
moneda_500=(m%500)/500
m=m%500
moneda_200=(m%200)/200
m=m%200
moneda_100=(m%100)/100
m=m%100
moneda_50=(m%50)/50
m=m%50
print("Estós son los billetes: ")
print("100k->",billete_100k)
print("50k->",billete_50k)
print("20k->",billete_20k)
print("10k->",billete_10k)
print("5k->",billete_5k)
print("2k->",billete_2k)
print("1k->",billete_1k)
print("Estás son las monedas: ")
print("500->",moneda_500)
print("200->",moneda_200)
print("100->",moneda_100)
print("50->",moneda_50)
#18.	Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántos horas minutos y segundos representan. Por ejemplo si el valor es 86399, imprimirá el siguiente resultado -->  23:59:59

num=int(input("Digíte los segundos: "))
hor=(int(num/3600))
minu=int((num-(hor*3600))/60)
seg=num-((hor*3600)+(minu*60))
print(str(hor)+"h "+str(minu)+"m "+str(seg)+"s")
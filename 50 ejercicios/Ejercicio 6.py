#6.	Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) de una venta realizada, indicando el valor original, el valor del IVA y el valor de la venta con IVA incluido.
valor=int(input("Dame tu valor de tu compra: "))
iva=0.19
ivaS=valor*iva
valor=ivaS+valor
print("Tú valor total es de: ",valor)
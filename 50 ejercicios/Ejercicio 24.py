#24.	Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) de una venta, si esta es mayor o igual 150.000 aplicar un descuento del 5%
precio=float(input("Digíta el precio del producto: "))
iva= precio*0.19
total=precio+iva
while total>=150000:
    descuento=total*0.05
    total=total-descuento
    break
print("El iva que tienes que pagar es de: $", iva)
print("El total que tienes que pagar: $",total)
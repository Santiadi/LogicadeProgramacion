#5. Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utiliza para ello una función que calcule la frecuencia del dígito en el número ingresado.
ef frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad
num=int(input("Escribe un número: "))
dig=int(input("Escribe un dígito: "))
print("La frecuencia del número es:", frecuencia(num, dig))
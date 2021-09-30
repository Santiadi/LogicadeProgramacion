#10.Escribir una función que, dada una cadena, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.  Consulta sobre la función len() en Python.
c=0
def lenPalabra(ca):
   if len(ca)==0:
       return 0
   for k in range(len(ca)):
       if ca[k]!=' ':
           c+=1
       else:
           if k<len(ca)-1 and ca[k+1]!=' ':
               c=0
   return c
ca = input("Ingrese la cadena o frase = ")
if lenPalabra(ca):
    print(lenPalabra(ca))

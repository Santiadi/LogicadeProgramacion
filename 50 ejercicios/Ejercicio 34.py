#34.	Escribe un algoritmo o el respectivo diagrama de flujo que, dado un usuario y una contraseña predefinida (por ejemplo usuario=”carlos" y contraseña=”1234”, le permita a un usuario digital su usuario y contraseña y enviar un mensaje de inicio de sesión si lo digitado corresponde al usuario y contraseña predefinida.
usuario=str(input("Digíte su usuario: "))
contraseña=int(input("Digíte su contraseña: "))
if contraseña==1234:
    print("Has iniciado sesión con exito "+usuario)
else:
    print("Digíte la contraseña de nuevo")
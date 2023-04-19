#                     Ejercicio 11
# Crea un programa con un bucle for y una sentencia break.
# El programa debe iterar sobre los caracteres en una dirección
# de correo electrónico, salir del bucle cuando llegue al símbolo @
# e imprimir la parte antes de @ en una línea.


lista = []
correo = input("Ingrese correo elecronico: ")
for i in correo:
    if i == "@":
        break
    else:
        lista.append(i)
seleccion = "".join(lista)
print(seleccion)

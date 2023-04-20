#                Ejercicio 12

# Crea un programa con un bucle for y una sentencia continue.
# El programa debe iterar sobre una cadena de dígitos,
# reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.


cadena = input("Ingrese valor: ")

for i in cadena:
    if i == "0":
        print("x", end="")
        continue
    else:
        print(i, end="")


# resuelto con listas y metodos

# lista = []
# cadena = input("ingrese valor: ")
# for i in cadena:
#     if i == "0":
#         lista.append("x")
#         continue
#     else:
#         lista.append(i)
# cadena_modificada = "".join(lista)
# print(cadena_modificada)

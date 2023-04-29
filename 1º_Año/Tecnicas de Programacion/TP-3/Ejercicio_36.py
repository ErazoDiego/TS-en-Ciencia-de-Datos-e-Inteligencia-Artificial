#                     Ejercicio 36

# Desarrollar un programa que permita cargar n números enteros
# y luego nos informe cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional
# (este operador retorna el resto de la división de dos valores,
# por ejemplo 11%2 retorna un 1, if valor%2==0: )


valores_pares = 0
valores_impares = 0
dato = int(input("Cantidad de numeros a ingresar: "))
for i in range(dato):
    numero = int(input("Ingrese numero: "))
    if numero % 2 == 0:
        valores_pares += 1
    else:
        valores_impares += 1
print("\nValores Pares: ", valores_pares, "\nValores Inpares: ", valores_impares)


# valores_pares = 0
# valores_impares = 0
# dato = 0
# while dato != "S":
#     dato = input(
#         "\n 'Ingrese una opcion' \n  'C' Para ingresar un numero: \n  'S' Para terminar: "
#     )
#     dato = dato.upper()
#     if dato == "S":
#         break
#     elif dato == "C":
#         dato = input("Ingrese numero: ")
#         dato = int(dato)
#         if dato % 2 == 0:
#             valores_pares += 1
#         else:
#             valores_impares += 1
#     else:
#         print("\nError de ingreso.")

# print("\nValores Pares: ", valores_pares, "\nValores Inpares: ", valores_impares)

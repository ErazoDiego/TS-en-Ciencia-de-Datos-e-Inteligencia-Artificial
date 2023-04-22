#                        Ejercicio 19

# Se ingresa por teclado un número entero positivo de uno o dos dígitos (1..99)
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)


numero = int(input("Ingrese numero de 1 o 2 digitos: "))
if numero >= 100:
    print("Error de ingreso")
else:
    if numero >= 10:
        print("El numero tiene 2 digitos")
    else:
        print("El numero tiene 1 solo digito")


# Prueba utilizando metodo len()

# numero = input("Ingrese numero de 1 o 2 digitos: ")
# if len(numero) >= 3:
#     print("Error de ingreso")
# else:
#     if len(numero) == 2:
#         print("El numero tiene 2 digitos")
#     else:
#         print("El numero tiene 1 solo digito")

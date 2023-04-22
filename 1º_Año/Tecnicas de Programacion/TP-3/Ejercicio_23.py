# Ejercicio 23

# Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
# y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
# Mostrar un mensaje de error si el número de cifras es mayor.

numero = int(input("Ingrese numero de hasta tres cifras: "))
if numero > 999:
    print("Error de ingreso")
elif numero >= 100:
    print("El numero tiene 3  cifras")
elif numero >= 10:
    print("El numero tiene 2 cifras")
else:
    print("El numero tiene 1 cifras")


# numero= input("Ingrese numero de hasta 3 cifras: ")
# if len(numero)>999:
#     print("Error de ingreso")
# elif len(numero)>=100:
#     print("El numero tiene 3  cifras")
# elif len(numero) >= 10:
#     print("El numero tiene 2 cifras")
# else:
#     print("El numero tiene 1 cifras")

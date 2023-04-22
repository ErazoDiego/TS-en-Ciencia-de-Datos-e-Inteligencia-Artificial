#                    Ejercicio 21

# Se cargan por teclado tres números distintos.
# Mostrar por pantalla el mayor de ellos.

# numero_1 = int(input("Ingrese numero 1: "))
# numero_2 = int(input("Ingrese numero 2: "))
# numero_3 = int(input("Ingrese numero 3: "))
# if numero_1 > numero_2:
#     if numero_1 > numero_3:
#         print("El mayor es: ", numero_1)
#     elif numero_3 > numero_1:
#         print("El mayor es: ", numero_3)
#     else:
#         print("El mayor es: ", numero_1)  # porque son iguales
# elif numero_2 > numero_3:
#     print("El mayor es: ", numero_2)
# else:
#     if numero_2 == numero_3:
#         print("El mayor es: ", numero_2)  # porque son iguales
#     else:
#         print("El mayor es: ", numero_3)


numero_1 = int(input("Ingrese numero 1: "))
numero_2 = int(input("Ingrese numero 2: "))
numero_3 = int(input("Ingrese numero 3: "))
mayor = 0
if numero_1 >= numero_2:
    if numero_1 >= numero_3:
        mayor = numero_1
    else:
        mayor = numero_3
elif numero_2 >= numero_3:
    mayor = numero_2
else:
    mayor = numero_3

print("El mayor es: ", mayor)

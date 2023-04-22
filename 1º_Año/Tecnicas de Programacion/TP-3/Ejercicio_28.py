#             Ejercicio 28

# Se ingresan por teclado tres números,
# si al menos uno de los valores ingresados es menor a 10,
# imprimir en pantalla la leyenda
# "Alguno de los números es menor a diez".

numero_1 = int(input("Ingrese numero 1: "))
numero_2 = int(input("Ingrese numero 2: "))
numero_3 = int(input("Ingrese numero 3: "))

if numero_1 < 10 or numero_2 < 10 or numero_3 < 10:
    print("Alguno de los números es menor a diez")
else:
    print("Aca no paso nada")

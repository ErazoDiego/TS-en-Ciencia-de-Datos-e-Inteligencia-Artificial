#             Ejercicio 27

# Se ingresan por teclado tres números,
# si todos los valores ingresados son menores a 10,
# imprimir en pantalla la leyenda "Todos los números son menores a diez".

numero_1 = int(input("Ingrese numero 1: "))
numero_2 = int(input("Ingrese numero 2: "))
numero_3 = int(input("Ingrese numero 3: "))

if numero_1 < 10 and numero_2 < 10 and numero_3 < 10:
    print("Todos los numeros son menores a 10")
else:
    print("Aca no paso nada")

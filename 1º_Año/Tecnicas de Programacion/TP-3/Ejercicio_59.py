#                 Ejercicio 59

# Crear y cargar una lista con 5 enteros.
# Implementar un algoritmo que identifique el mayor valor de la lista.

my_list = []

for i in range(0, 5):
    dato = int(input("Ingrese un numero: "))
    my_list.append(dato)
mayor = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > mayor:
        mayor = my_list[i]

print("\nEl mayor de la lista es: ", mayor)

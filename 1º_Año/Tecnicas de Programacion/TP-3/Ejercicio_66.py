#                     Ejercicio 66

# Se debe crear y cargar una lista donde almacenar 5 sueldos.
# Ordenar de menor a mayor la lista.

my_list = []
for i in range(0, 5):
    dato = float(input("Ingrese sueldo: "))
    my_list.append(dato)
my_list.sort()
print("\nLista ordenada:\n", my_list)

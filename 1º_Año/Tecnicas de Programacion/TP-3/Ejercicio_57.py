#                     Ejercicio 57

# Almacenar en una lista los sueldos (valores float) de 5 operarios.
# Imprimir la lista y el promedio de sueldos.

my_list = []
promedio = 0
for i in range(0, 5):
    dato = float(input("Ingrese Sueldo: "))
    my_list.append(dato)
    promedio += my_list[i]
promedio = promedio / len(my_list)
print("Lista: ", my_list, "\nPromedio: ", promedio)

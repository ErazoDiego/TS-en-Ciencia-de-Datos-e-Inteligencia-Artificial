#             Ejercicio 51

# Definir una lista que almacene 5 enteros.
# Sumar todos sus elementos y mostrar dicha suma.

my_list = [2, 4, 6, 8, 10]
suma = 0
for i in range(len(my_list)):
    suma += my_list[i]
print(suma)

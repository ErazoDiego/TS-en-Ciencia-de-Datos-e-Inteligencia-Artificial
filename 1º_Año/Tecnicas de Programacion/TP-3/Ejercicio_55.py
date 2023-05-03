#                     Ejercicio 55

# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado
# y añadirlos a la lista.
# Imprimir la lista generada.

my_list = []
for i in range(0, 5):
    dato = int(input("Ingrese un numero: "))
    my_list.append(dato)
print(my_list)

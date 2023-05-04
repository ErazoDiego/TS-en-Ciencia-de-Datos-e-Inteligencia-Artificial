#                         Ejercicio 56

# Realizar la carga de valores enteros por teclado,
# almacenarlos en una lista.
# Finalizar la carga de enteros al ingresar el cero.
# Mostrar finalmente la lista y su tamaño.


lista = []
dato = 1
while dato != 0:
    dato = int(input("Ingrese un numero: "))
    if dato != 0:
        lista.append(dato)
print("Lista: ", lista, "\nTamaño: ", len(lista))

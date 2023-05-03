#                     Ejercicio 60

# Crear y cargar una lista con 5 enteros por teclado.
# Implementar un algoritmo que identifique el menor valor de la lista
# y la posición donde se encuentra.

my_list = []
menor = 999999999
posicion = 0
for i in range(0, 5):
    dato = int(input("Ingrese un numero: "))
    my_list.append(dato)

for i in range(len(my_list)):
    if my_list[i] < menor:
        menor = my_list[i]
        posicion = i

print("\nEl menor de la lista es: ", menor, "\nEsta en la posicion: ", posicion)

#                             Ejercicio 39

# Imprimir todos los números impares que hay entre 1 y 100. Resolverlo empleando for.


for i in range(1, 101):
    if i % 2 == 0:
        continue
    else:
        print(i, end=" ")

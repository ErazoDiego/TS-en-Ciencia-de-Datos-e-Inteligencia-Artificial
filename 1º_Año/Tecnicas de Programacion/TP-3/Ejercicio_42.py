#                 Ejercicio 42

# Desarrollar un programa que solicite la carga de 10 números
# e imprima la suma de los últimos 5 valores ingresados.
# Resolverlo empleando for.

suma = 0
for i in range(10):
    numero = int(input("Ingrese numero: "))
    if i >= 5:
        suma += numero
    else:
        continue
print("la suma de los ultimos 5 numeros es: ", suma)

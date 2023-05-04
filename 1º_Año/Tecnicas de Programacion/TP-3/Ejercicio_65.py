#                         Ejercicio 65

# Realizar un programa que pida la carga de dos listas
# numéricas enteras de 4 elementos cada una.
# Generar una tercer lista que surja de la suma de los elementos
# de la misma posición de cada lista.
# Mostrar esta tercer lista.

lista_1 = []
lista_2 = []
lista_suma = []
print("lista 1")
for i in range(0, 4):
    dato = int(input("ingrese numero: "))
    lista_1.append(dato)
print("\nlista 2")
for i in range(0, 4):
    dato = int(input("ingrese numero: "))
    lista_2.append(dato)
for i in range(len(lista_1)):
    dato = lista_1[i] + lista_2[i]
    lista_suma.append(dato)
print("\nlista suma:\n", lista_suma)

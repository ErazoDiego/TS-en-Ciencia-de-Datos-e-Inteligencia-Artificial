#                 Ejercicio 50

# ¿Cuál es el resultado del siguiente fragmento de código?

# a)
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[0]

print(list_3)

# RESPUESTA
# ["C"]

# ----------------------------------

# b)
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2

print(list_3)

# RESPUESTA
# ["B","C"]

# ----------------------------------

# c)
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[:]

print(list_3)

# RESPUESTA
# []

# ----------------------------------

# d)
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
del list_1[0]
del list_2[0]

print(list_3)

# RESPUESTA
# []

# ----------------------------------

# e)
# Inserta in o not in en lugar de ???
# para que el código genere el resultado esperado.

my_list = [1, 2, "in", True, "ABC"]
print(1 in my_list)
print("A" not in my_list)
print(3 not in my_list)
print(False in my_list)

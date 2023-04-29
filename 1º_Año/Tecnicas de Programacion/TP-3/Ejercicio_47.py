#                         Ejercicio 47

# ¿Cuál es el resultado de los siguientes fragmentos de código?

# a)
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)

# RESPUESTA
# [6,2,3,4,5,1]

# -----------------------------------

# b)
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

# RESPUESTA
# [1,3,6,10,15]

# -----------------------------------

# c)
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

# RESPUESTA
# [2,3]
# 3

# -----------------------------------

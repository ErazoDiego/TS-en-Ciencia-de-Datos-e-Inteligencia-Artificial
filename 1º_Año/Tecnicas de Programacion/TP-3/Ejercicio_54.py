#                     Ejercicio 54

# Definir por asignación una lista con 8 elementos enteros.
# Contar cuantos de dichos valores almacenan un valor superior a 100.
contador = 0
my_list = [25, 200, 655, 120, 10, 1, 100, 500]
for i in range(len(my_list)):
    if my_list[i] > 100:
        contador += 1
print(contador, " valores mayores a 100")

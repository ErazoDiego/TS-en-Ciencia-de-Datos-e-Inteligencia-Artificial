#                     Ejercicio 49

# Escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.
# Nota: Asume que la lista original está ya dentro del código - no tienes que ingresarla desde el teclado.
# Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal - no necesitas actualizar la lista actual.
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lst = []
for valor in my_list:
    if valor not in lst:
        lst.append(valor)
print(lst)

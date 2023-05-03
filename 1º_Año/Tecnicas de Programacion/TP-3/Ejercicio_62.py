#                         Ejercicio 62

# Cargar una lista con 5 elementos enteros.
# Imprimir el mayor y un mensaje si se repite dentro de la lista
# (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

my_list = []
mayor = -999999999
contador = 0
mensaje = ""
for i in range(0, 5):
    dato = int(input("Ingrese un numero: "))
    my_list.append(dato)

for i in range(len(my_list)):
    if my_list[i] > mayor:
        mayor = my_list[i]
for i in range(len(my_list)):
    if mayor == my_list[i]:
        contador += 1

if contador > 1:
    mensaje = "El numero se encuentra 2 o mas veces"
else:
    mensaje = "El numero no se repirte"
print("\nEl mayor es: ", mayor, "\n", mensaje)

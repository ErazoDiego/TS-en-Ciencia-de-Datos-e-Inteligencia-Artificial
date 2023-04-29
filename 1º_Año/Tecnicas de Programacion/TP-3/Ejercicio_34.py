#                 Ejercicio 34

# Se ingresan un conjunto de n alturas de personas por teclado.
# Mostrar la altura promedio de las personas.


promedio = 0
alturas = 0
contador = 0
cantidad_datos = int(input("Ingrese la cantidad de alturas a ingresar: "))
while contador < cantidad_datos:
    dato = float(input("Ingrese altura: "))
    alturas += dato
    contador += 1
promedio = alturas / cantidad_datos
print("El promedio es: ", promedio)


# promedio = 0
# contador = 0
# dato = 0
# alturas = 0
# while dato != "s":
#     dato = input("Ingrese altura o 's' para salir: ")
#     if dato != "s":
#         alturas += float(dato)
#         contador += 1
# promedio = alturas / contador
# print("El promedio es: ", promedio)

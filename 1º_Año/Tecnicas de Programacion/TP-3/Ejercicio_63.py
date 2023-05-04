#                         Ejercicio 63

# Desarrollar un programa que permita cargar 5 nombres de personas
# y sus edades respectivas.
# Luego de realizar la carga por teclado de todos los datos
# imprimir los nombres de las personas mayores de edad
# (mayores o iguales a 18 años)

lista = []
mayores = []
nombre = ""
edad = 0
for i in range(0, 5):
    nombre = input("\nIngrese Nombre: ")
    edad = int(input("Ingrese Edad: "))
    lista.append([nombre, edad])

for i in range(len(lista)):
    if lista[i][1] >= 18:
        mayores.append(lista[i][0])

print("\nMayores de 18: \n", mayores)

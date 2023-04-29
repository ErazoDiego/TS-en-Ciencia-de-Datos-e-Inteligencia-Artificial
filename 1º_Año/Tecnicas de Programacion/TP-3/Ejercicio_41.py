#                                 Ejercicio 41

# Confeccionar un programa que lea n pares de datos,
# cada par de datos corresponde a la medida de la base y la altura de un triángulo.
# Resolverlo empleando for.
# El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

base = 0
altura = 0
superficie = 0
triangulos_mayor = 0
cantidad_datos = int(input("Ingrese la cantidad de datos a ingresar: "))
for i in range(cantidad_datos):
    base = float(input("\nIngrese medida de la base: "))
    altura = float(input("Ingrese altura: "))
    superficie = base * altura
    print("\nBase: ", base, "\nAltura: ", altura, "\nSuperficie: ", superficie)
    if superficie > 12:
        triangulos_mayor += 1
    else:
        continue
print("\nTriangulos con superficie mayor a 12: ", triangulos_mayor)

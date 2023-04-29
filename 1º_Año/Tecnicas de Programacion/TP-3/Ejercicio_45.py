#                         Ejercicio 45

# Realizar un programa que lea los lados de n triángulos,
# Resolverlo empleando for, e informar:

# a) De cada uno de ellos, qué tipo de triángulo es:
#     equilátero (tres lados iguales),
#     isósceles (dos lados iguales),
#     o escaleno (ningún lado igual)

# b) Cantidad de triángulos de cada tipo.

triangulos_equilateros = 0
triangulos_isosceles = 0
triangulos_escaleno = 0
dato = int(input("Cantidad de tiangulos a ingresar: "))
for i in range(dato):
    lado_1 = float(input("\nIngrese lado 1: "))
    lado_2 = float(input("Ingrese lado 2: "))
    lado_3 = float(input("Ingrese lado 3: "))
    if lado_1 == lado_2 and lado_1 == lado_3:
        triangulos_equilateros += 1
        print("Es un triangulo Equilatero.")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        triangulos_isosceles += 1
        print("Es un triangulo Isosceles.")
    else:
        triangulos_escaleno += 1
        print("Es un triangulo Escaleno.")
print(
    "\nTriangulos Equilateros: ",
    triangulos_equilateros,
    "\nTriangulos Isosceles: ",
    triangulos_isosceles,
    "\nTriangulos Escalenos: ",
    triangulos_escaleno,
)

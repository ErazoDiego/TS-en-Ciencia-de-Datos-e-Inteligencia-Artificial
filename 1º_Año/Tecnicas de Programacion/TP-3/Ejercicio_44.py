#                          Ejercicio 44

# Confeccionar un programa que permita ingresar un valor del 1 al 10
# y nos muestre la tabla de multiplicar del mismo (los primeros 10 términos)
# Resolverlo empleando for.
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30


valor = int(input("Ingrese un valor: "))
for i in range(1, 11):
    calculo = valor * i
    print(valor, "x", i, "=", calculo)

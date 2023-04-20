# Ejercicio 16
# Realizar un programa que solicite ingresar dos números distintos
# y muestre por pantalla el mayor de ellos.

num_a = int(input("Ingrese un numero: "))
num_b = int(input("Ingrese un segundo numero: "))

if num_a != num_b:
    if num_a > num_b:
        print("El numero", num_a, "es mayor que", num_b)
    else:
        print("El numero", num_b, "es mayor que", num_a)
else:
    print("Los numero son iguales")

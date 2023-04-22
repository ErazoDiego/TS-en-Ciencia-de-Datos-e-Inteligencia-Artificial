#           Ejercicio 22

# Se ingresa por teclado un valor entero,
# mostrar una leyenda que indique si el número es positivo,
# negativo o nulo (es decir cero)

numero = int(input("Ingrese un numero entero: "))
if numero == 0:
    print("El valor ingresado es nulo")
elif numero < 0:
    print("El valr ingresado es negativo")
else:
    print("El valr ingresado es positivo")

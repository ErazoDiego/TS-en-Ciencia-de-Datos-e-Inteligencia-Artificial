
#                                 Ejercicio 18

# Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el
# cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los
# mismos. LLamar desde el bloque del programa principal a ambas funciones.

def calcular_cuadrado():
    dato = int(input("Ingrese un numero: "))
    cuadrado = dato**2
    return cuadrado


def calcular_producto():
    dato_1 = int(input("Ingrese 1º numero: "))
    dato_2 = int(input("Ingrese 2º numero: "))
    producto = dato_1*dato_2
    return producto


print(calcular_cuadrado())
print(calcular_producto())

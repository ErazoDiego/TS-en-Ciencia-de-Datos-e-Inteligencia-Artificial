#                 Ejercicio 32

# Codificar un programa que solicite la carga de un valor positivo
# y nos muestre desde 1 hasta el valor ingresado de uno en uno.
# Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30.


valor = -1
i = 1
while valor <= 0:
    valor = int(input("Ingrese un valor entero positivo: "))
    if valor <= 0:
        print('\n"..Error de ingreso.."')
        continue
    else:
        while i <= valor:
            print(i, end=" ")
            i += 1

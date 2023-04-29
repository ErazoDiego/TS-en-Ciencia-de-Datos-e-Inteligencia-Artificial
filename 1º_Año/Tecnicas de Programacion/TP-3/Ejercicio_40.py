#                     Ejercicio 40

# Escribir un programa que lea 10 números enteros y luego muestre
# cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5.
# Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
# Resolverlo empleando for.

multiplos_3 = 0
multiplos_5 = 0
for i in range(11):
    dato = int(input("Ingrese un numero: "))
    if dato % 3 == 0:
        multiplos_3 += 1
    if dato % 5 == 0:
        multiplos_5 += 1
    else:
        continue
print("\nMultiplos de 3: ", multiplos_3, "\nMultiplos de 5: ", multiplos_5)

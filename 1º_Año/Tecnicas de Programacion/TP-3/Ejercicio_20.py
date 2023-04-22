#               Ejercicio 20

# Confeccionar un programa que pida por teclado tres notas de un alumno,
# calcule el promedio e imprima alguno de estos mensajes:
# Si el promedio es >=7 mostrar "Promocionado".
# Si el promedio es >=4 y <7 mostrar "Regular".
# Si el promedio es <4 mostrar "Reprobado".

nota_2 = int(input("Ingrese 2ª nota: "))
nota_1 = int(input("Ingrese 1ª nota: "))
nota_3 = int(input("Ingrese 3ª nota: "))
promedio = (nota_1 + nota_2 + nota_3) / 3
if promedio >= 7:
    print("Promocionado")
elif promedio >= 4 and promedio < 7:
    print("Regular")
else:
    print("Reprobado")

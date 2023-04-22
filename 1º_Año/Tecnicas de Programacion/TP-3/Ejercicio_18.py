#           Ejercicio 18

# Se ingresan tres notas de un alumno,
# si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

nota_1 = int(input("ingrese 1ª nota: "))
nota_2 = int(input("Ingrese 2ª nota: "))
nota_3 = int(input("ingrese 3ª nota: "))

promedio = (nota_1 + nota_2 + nota_3) / 3
if promedio >= 7:
    print('"Promociona""')
else:
    print('"No promociona"')

#                 Ejercicio 33

# Escribir un programa que solicite ingresar 10 notas de alumnos
# y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

notas_mayores = 0
notas_menores = 0
for i in range(10):
    nota = int(input("Ingrese nota: "))
    if nota >= 7:
        notas_mayores += 1
    else:
        notas_menores += 1
print("Cantidad de aprovados: ", notas_mayores)
print("Cantidad de desaprovados: ", notas_menores)

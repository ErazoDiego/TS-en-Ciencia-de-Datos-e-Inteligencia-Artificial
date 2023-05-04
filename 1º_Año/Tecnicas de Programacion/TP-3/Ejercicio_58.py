#                     Ejercicio 58

# Una empresa tiene dos turnos (mañana y tarde)
# en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde)
# Confeccionar un programa que permita almacenar los sueldos de los empleados
# agrupados en dos listas.
# Imprimir las dos listas de sueldos.

empleados_grupo2 = []
empleados_grupo1 = []
turno = ""
for i in range(0, 4):
    dato = float(input("Ingrese sueldo turno mañana: "))
    empleados_grupo1.append(dato)
for i in range(0, 4):
    dato = float(input("Ingrese sueldo turno tarde: "))
    empleados_grupo2.append(dato)

print("Empleados Mañana: ", empleados_grupo1, "\nEmpleados Tarde: ", empleados_grupo2)

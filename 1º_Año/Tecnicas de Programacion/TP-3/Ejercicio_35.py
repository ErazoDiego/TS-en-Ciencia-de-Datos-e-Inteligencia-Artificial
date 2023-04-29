#                         Ejercicio 35

# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
# realizar un programa que lea los sueldos que cobra cada empleado e informe
# cuántos empleados cobran entre $100 y $300 ycuántos cobran más de $300.
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

sueldos_bajos = 0
sueldos_altos = 0
gasto_total = 0
dato = int(input("Ingrese cantidad de sueldos a ingresar: "))
for i in range(dato):
    sueldo = float(input("Ingrese sueldo: "))
    if sueldo <= 300:
        sueldos_bajos += 1
        gasto_total += sueldo
    else:
        sueldos_altos += 1
        gasto_total += sueldo
print(
    "\nEmpleados que cobran entre 100 y 300: ",
    sueldos_bajos,
    "\nEmpleados que cobran mas de 300: ",
    sueldos_altos,
    "\nEl importe de la empresa en sueldos es: ",
    gasto_total,
)


# sueldos_bajos = 0
# sueldos_altos = 0
# gasto_total = 0
# dato = 0
# while dato != "s":
#     dato = input(
#         "\n 'Ingrese una opcion' \n  'c' Para ingresar un sueldo \n  's' Para terminar: "
#     )
#     dato = dato.upper()
#     if dato == "S":
#         break
#     elif dato == "C":
#         dato = input("Ingrese sueldo: ")
#         dato = float(dato)
#         if dato <= 300:
#             sueldos_bajos += 1
#             gasto_total += dato
#         else:
#             sueldos_altos += 1
#             gasto_total += dato
#     else:
#         print("\nError de ingreso.")

# print(
#     "\nEmpleados que cobran entre 100 y 300: ",
#     sueldos_bajos,
#     "\nEmpleados que cobran mas de 300: ",
#     sueldos_altos,
#     "\nEl importe de la empresa en sueldos es: ",
#     gasto_total,
# )

#                                     Ejercicio 67

# Confeccionar un programa que permita cargar los nombres de 5 alumnos
# y sus notas respectivas.Luego ordenar las notas de mayor a menor.
# Imprimir las notas y los nombres de los alumnos.
# Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas de mayor a menor
# debemos intercambiar los nombres para que las listas continúen paralelas
# (es decir que en los mismos subíndices de cada lista continúe la información relacionada)

lst_nombres = []
lst_notas = []
intercambio = True
for i in range(0, 5):
    nombre = input("\nIngrese Nombre: ")
    nota = float(input("Ingrese Nota: "))
    lst_nombres.append(nombre)
    lst_notas.append(nota)

while intercambio == True:
    intercambio = False
    for i in range(len(lst_notas) - 1):
        if lst_notas[i] < lst_notas[i + 1]:
            lst_notas[i], lst_notas[i + 1] = lst_notas[i + 1], lst_notas[i]
            lst_nombres[i], lst_nombres[i + 1] = (
                lst_nombres[i + 1],
                lst_nombres[i],
            )
            intercambio = True

for i in range(len(lst_notas)):
    print("'", lst_nombres[i], lst_notas[i], "'", end=" ")

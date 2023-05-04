#                 Ejercicio 64

# En un curso de 4 alumnos se registraron las notas de sus exámenes
# y se deben procesar de acuerdo a lo siguiente:

# a) Ingresar nombre y nota de cada alumno
# (almacenar los datos en dos listas paralelas)

# b) Realizar un listado que muestre los nombres,
# notas y condición del alumno. En la condición,
# colocar "Muy Bueno" si la nota es mayor o igual a 8,
# "Bueno" si la nota está entre 4 y 7, y colocar
# "Insuficiente" si la nota es inferior a 4.

# c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

lista_alumnos = []
lista_notas = []
contador = 0
nombre = ""
nota = 0
for i in range(0, 4):
    nombre = input("Ingrese Nombre: ")
    nota = float(input("Ingrese Nota: "))
    lista_alumnos.append(nombre)
    lista_notas.append(nota)

for i in range(len(lista_notas)):
    if lista_notas[i] >= 8:
        mensaje = " Muy bueno"
        contador += 1
    elif lista_notas[i] < 7 and lista_notas[i] >= 4:
        mensaje = " Bueno"
    else:
        mensaje = " Insuficiente"
    print("\nNombre:", lista_alumnos[i], " Nota:", lista_notas[i], mensaje)
print("\nAlumnos con 'Muy Bueno': ", contador)

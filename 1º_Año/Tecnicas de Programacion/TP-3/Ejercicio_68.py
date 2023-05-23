#                         Ejercicio 68

# Crear y cargar en un lista los nombres de 5 países
# y en otra lista paralela la cantidad de habitantes del mismo.
# Ordenar alfabéticamente e imprimir los resultados.
# Por último ordenar con respecto a la cantidad de habitantes
# (de mayor a menor) e imprimir nuevamente.

lst_paises = []
lst_habitantes = []

for i in range(0, 5):
    dato = input("Ingrese Nombre: ")
    lst_paises.append(dato)
    dato = int(input("Ingrese cantidad de habitantes: "))
    lst_habitantes.append(dato)

intercambio = True
while intercambio == True:
    intercambio = False
    for i in range(len(lst_paises) - 1):
        if lst_paises[i] > lst_paises[i + 1]:
            lst_paises[i], lst_paises[i + 1] = lst_paises[i + 1], lst_paises[i]
            lst_habitantes[i], lst_habitantes[i + 1] = (
                lst_habitantes[i + 1],
                lst_habitantes[i],
            )
            intercambio = True


print("\nPaises:    Habitantes: ")
for i in range(len(lst_paises)):
    print("", lst_paises[i], "      ", lst_habitantes[i])
intercambio_2 = True
while intercambio_2 == True:
    intercambio_2 = False
    for i in range(len(lst_habitantes) - 1):
        if lst_habitantes[i] < lst_habitantes[i + 1]:
            lst_habitantes[i], lst_habitantes[i + 1] = (
                lst_habitantes[i + 1],
                lst_habitantes[i],
            )
            lst_paises[i], lst_paises[i + 1] = lst_paises[i + 1], lst_paises[i]
            intercambio_2 = True

print("\nPaises:    Habitantes: ")
for i in range(len(lst_paises)):
    print("", lst_paises[i], "      ", lst_habitantes[i])

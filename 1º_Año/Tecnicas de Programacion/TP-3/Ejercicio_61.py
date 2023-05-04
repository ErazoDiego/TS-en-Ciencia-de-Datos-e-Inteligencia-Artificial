#                         Ejercicio 61

# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
# Mostrar el nombre de persona menor en orden alfabético.

my_list = []
for i in range(0, 5):
    dato = input("Ingrese un Nombre: ")
    my_list.append(dato)
my_list.sort()
print("\nLista: ", my_list)

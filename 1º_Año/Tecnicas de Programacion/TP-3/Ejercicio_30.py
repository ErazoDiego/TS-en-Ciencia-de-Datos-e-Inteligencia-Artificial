#                 Ejercicio 30

# De un operario se conoce su sueldo y los años de antigüedad.
# Se pide confeccionar un programa que lea los datos de entrada e informe:

# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años,
#    otorgarle un aumento del 20 %, mostrar el sueldo a pagar.

# b) Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.

# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

aumento = 0
sueldo = int(input("Ingrese sueldo: "))
antiguedad = int(input("Ingrese años de antiguedad: "))
if sueldo < 500 and antiguedad >= 10:
    aumento = (20 * sueldo) / 100
    sueldo = sueldo + aumento
    print("El sueldo a pagar sera de: $", sueldo)
elif sueldo < 500 and antiguedad < 10:
    aumento = (5 * sueldo) / 100
    sueldo = sueldo + aumento
    print("El sueldo a pagar sera de: $", sueldo)
else:
    print("El sueldo a pagar sera de: $", sueldo)

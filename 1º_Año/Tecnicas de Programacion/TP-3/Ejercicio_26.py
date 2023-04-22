#             Ejercicio 26

# Realizar un programa que pida cargar una fecha cualquiera,
# luego verificar si dicha fecha corresponde a Navidad.

dia = int(input("Ingrese dia: "))
if dia > 0 and dia <= 31:
    mes = int(input("Ingrese mes: "))
    if mes > 0 and mes <= 12:
        if dia == 25 and mes == 12:
            print("La fecha corresponde a NAVIDAD")
        else:
            print("La fecha no corresponde a la NAVIDAD")
    else:
        print("Error de ingreso")
else:
    print("Error de ingreso")

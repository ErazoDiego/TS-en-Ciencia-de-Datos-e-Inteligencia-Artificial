#         Ejercicio 25

# Se carga una fecha (día, mes y año) por teclado.
# Mostrar un mensaje si corresponde al primer trimestre del año
# (enero, febrero o marzo) Cargar por teclado el valor numérico del día, mes y año.

# dia = int(input("Ingrese dia: "))
# mes = input("Ingrese mes: ")
# anio = int(input("Ingrese año: "))
# mes = mes.upper()
# if mes == "ENERO" or mes == "FEBRERO" or mes == "MARZO":
#     print("La fecha indicada pertenece al primer trimestre del año")
# else:
#     print("La fecha indicada NO pertenece al primer trimestre del año")


dia = int(input("Ingrese dia: "))
if dia <= 0 or dia > 32:
    print("Error de ingreso")
else:
    mes = int(input("Ingrese mes: "))
    if mes <= 0 and mes > 12:
        print("Error de ingreso")
    else:
        anio = int(input("Ingrese año: "))
        if anio >= 0:
            if mes <= 3:
                print("La fecha indicada pertenece al primer trimestre del año")
            else:
                print("La fecha indicada NO pertenece al primer trimestre del año")
        else:
            print("La fecha indicada NO pertenece al primer trimestre del año")

#                 Ejercicio 29

# Escribir un programa que pida ingresar la coordenada de un punto en el plano,
# es decir dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
# (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

cordenada_x = int(input("Ingrese cordenada x: "))
cordenada_y = int(input("Ingrese cordenada y: "))
if cordenada_x != 0 and cordenada_y != 0:
    if cordenada_x > 0 and cordenada_y > 0:
        print(" El punto se ubica en el 1º Cuadrante")
    elif cordenada_x < 0 and cordenada_y > 0:
        print(" El punto se ubica en el 2º Cuadrante")
    elif cordenada_x < 0 and cordenada_y < 0:
        print(" El punto se ubica en el 3º Cuadrante")
    else:
        print(" El punto se ubica en el 4º Cuadrante")
else:
    print("Uno de los datos ingresados es 0")

# Ejercicio 15
# Ingresar el sueldo de una persona,
# si supera los 3000 dolares mostrar un mensaje en pantalla indicando
# que debe abonar impuestos.

sueldo = int(input("Ingrese su sueldo es usd: "))

if sueldo >= 3000:
    print("DEBE DE PAGAR IMPUESTOS")
else:
    print("Esta OK")

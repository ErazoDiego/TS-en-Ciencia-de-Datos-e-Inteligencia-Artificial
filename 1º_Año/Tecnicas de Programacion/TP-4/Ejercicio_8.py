
#                 Ejercicio 8
# ¿Cuál es la salida de los siguientes fragmentos de código?

# a)
def message():
    alt = 1
    print("¡hola, mundo!")


# print(alt)
# Respuesta:alt is not defined

# -----------#------------#------------#-----------#-------------#

# b)
a = 1


def fun():
    a = 2
    print(a)


print("Respuesta b)_")
fun()
print(a)
# Respuesta:
# 2
# 1

# -----------#------------#------------#-----------#-------------#


# c)
a = 1


def fun():
    global a
    a = 2
    print(a)


print("\nRespuesta c)_")
fun()
a = 3
print(a)

# Respuesta:
# 2
# 3

# -----------#------------#------------#-----------#-------------#

# d)
a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
print("\nRespuesta d)_")
fun()
print(a)
# Respuesta:
# 2
# 3

# -----------#------------#------------#-----------#-------------#

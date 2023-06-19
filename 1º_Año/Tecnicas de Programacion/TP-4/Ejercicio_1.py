#             Ejercicio 1

# ¿Cuál es la salida de los siguientes fragmentos de código?

# a)
def intro(a="James Bond", b="bond"):
    print("Mi nombre es: ", b + ".", a + ".")


intro()
# Respuesta
# Mi nombre es:  bond. James Bond.


# b)
def intro(a="James Bond", b="bond"):
    print("Mi nombre es: ", b + ".", a + ".")


intro("Sean Connery")
# Respuesta
# Mi nombre es:  bond. Sean Connery.

# c)
def intro(a, b="bond"):
    print("Mi nombre es: ", b + ".", a + ".")


intro("Susan")
# Respuesta
# Mi nombre es:  bond. Susan.


# d)
# def add_numbers(a, b=2, c):#( 'c' deveria estar antes que 'b')
#     print(a+b+c)

# add_numbers(a=1,C=3)
# Respuesta
# ERROR de argumento no asignado

# Forma correcta
def add_numbers(a, c, b=2):  #
    print(a + b + c)


add_numbers(a=1, c=3)
# Respuesta

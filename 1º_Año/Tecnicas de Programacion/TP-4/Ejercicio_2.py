#                 Ejercicio 2

# ¿Cuál es la salida de los siguientes fragmentos de código?

# a)
def hi():
    return
    print("¡Hola!")


hi()
# Respuesta
# No realiza nada porque el retur esta antes del print

# --------------------#--------------------#-------------------#-------------------#-------------------#-------------------#
# b)
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False


print(is_int(5))
print(is_int(5.0))
print(is_int("5"))

# Respuesta
# True
# False
# None

# --------------------#--------------------#-------------------#-------------------#-------------------#-------------------#

# c)
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst


print(even_num_lst(11))

#Respuesta
#[0, 2, 4, 6, 8, 10]

# --------------------#--------------------#-------------------#-------------------#-------------------#-------------------#

#d)
def list_updater(lst):
    upd_list=[]
    for elem in lst:
        elem **=2
        upd_list.append(elem)
    return upd_list

foo=[1,2,3,4,5]
print(list_updater(foo))

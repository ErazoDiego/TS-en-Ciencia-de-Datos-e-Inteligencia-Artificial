# Ejercicio 13
# ¿Cuál es el output de los siguientes códigos?

# a)
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
#   4
#   3
#   2
#   0

# b)
n = range(4)
for num in n:
    print(num - 1)
else:
    print(num)
#   -1
#   0
#   1
#   2
#   3

# c)
for i in range(0, 6, 3):
    print(i)
#   0
#   3

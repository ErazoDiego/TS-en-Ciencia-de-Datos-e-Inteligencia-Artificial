#               Ejercicio 5

# ¿Cuál es el resultado del siguiente fragmento de código?

# a)
#    a.1 folse
#    a.2 true
print("\n a)")
x = 5
y = 10
z = 8
print(x > y)
print(y > z)


# b)
#    b.1 folse
#    b.2 true
print("\n b)")
x, y, z = 5, 10, 8
print(x > z)
print((y - 5) == x)


# c)
#    c.1 true
#    c.2 folse
print("\n c)")
x, y, z = 5, 10, 8
x, y, z = z, y, x
print(x > z)
print((y - 5) == x)


# d)
#    true
#    true
#    else
print("\n d)")
x = 10
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

# e)
#   four
#   five
print("\n e)")
x = "1"
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")


# f)
#   one
#   two
print("\n f)")
x = 1
y = 1.0
z = "1"
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

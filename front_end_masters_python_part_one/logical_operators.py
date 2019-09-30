######################
##Logical operators ##
######################

a = True
b = True

print(a and b)

a = [1]
b = [2]

print(a and b)

a = False
b = True

print(a and b)

a = False
b = False

print(a and b)

a = []
b = {1}

print(a and b)

a = []
b = [2]

print(a or b)

x = 2
if not x:
    print("x is empty")
else:
    print("x has a value")
a = 0
b = 1

print(a or b)

print(not True)

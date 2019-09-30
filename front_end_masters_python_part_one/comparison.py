#####################
# Basic comparism   #
#####################

print("====Integer comparison====")
print(2 == 2)
print(2 < 2)
print(3 > 5)
print(4 >= 6)
print(10 <= 5)

# Upper case letters are lower-valued in ASCII
print("====String comparison====")
print("T" < "t")
print("t" < "T")

print("a" < "b")
print("bat" < "cat")
print(1 == 1)
print("Hello" == "Hello")

# Advance datastructure comparism
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [1, 2, 4])

# Note: identity is different from equality
a = 10
b = 20
print(a != b)

x = None
if x:
    print(f"x is not empty")
else:
    print(f"x is empty")

print(a is b)
print(a is not None)

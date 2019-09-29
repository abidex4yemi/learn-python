####################
# Tuples basics    #
####################

# Tuples are immutable: once created the items in it cant be change

a = ()
print(type(a))

# Note: comma is mandatory and parenthesis can be omitted
b = (1,)
print(type(b))

numbers = 1, 2, 3, 4, 5, 6, 67, 8
print(numbers)

students = ("Mercy", 8, "History", 3.5)
print(students[0])
print(students[1])

# tuples immutability
# this will throw this error
# ypeError: 'tuple' object does not support item assignment
# students[0] = "Yemi"

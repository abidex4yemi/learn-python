#####################
#      Set basics   #
#####################

# An empty braces {} will give type dictionary
names = {}

# print(type({}))

# To create an empty set set() must be called explicitly
# print(set())

numbers = {1, 1, 3, 4, 5, 5, 6, 6, 7}
# print(numbers)

# Remove the first item in set
numbers.pop()
# print(numbers)

# if member does not exist raise key error
# print(numbers.remove(7))
# print(numbers)

# Note set will ignore duplicate value
friends = {"Yemi", "Jane", "Yemi", "Lola"}
# print(friends)
# print(len(friends))

# This will throw error
# TypeError: 'set' object is not subscriptable
# friend = friends[0]
# print(friends)

# We can check for hash of a specific value
print(hash("John"))

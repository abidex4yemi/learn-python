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
# print(hash("John"))

########################################
# Adding, removing, updating in set()  #
########################################

# Adding #

colors = {"Red", "Green", "Blue"}
# print(colors)

colors.add("Yellow")
# print(colors)

# Removing #

# Major difference between discard() and remove is if
# value does not exist when using discard() it does not throw error
# but remove() will throw error
# colors.remove("red")

colors.remove("Red")
# print(colors)

colors.discard("Green")
# print(colors)

# Updating #

students = {"Shola", "Jane"}

new_students = {"Lee", "John", "Nina"}

students.update(new_students)

# print(students)

# Note: update() expect sequence if passed commam separated values
# the value will be splitted e.g "Yemi" => "Y", "e", "m", "i"
students.update({"Tom", "Lola"})
# print(students)

# Reading value #

# for friend in friends:
#     print(friend)


########################################
# Combining, Comparing, contrasting  #
########################################

# Set operations

# Comparing #
#############

colors = {"Red", "Green", "Blue", "Maroon"}

# print("Red" in colors)
# print("Yellow" in colors)

# Combining #
#############

rainbow_colors = {"Red", "Orange", "Yellow", "Green", "Blue", "Violet"}
favorite_colors = {"Pink", "Black", "Blue"}

# my_set.union(other_set)
all_colors = rainbow_colors.union(favorite_colors)
# print(all_colors)

# my_set | other_set
all_colors = rainbow_colors | favorite_colors
# print(all_colors)

# Intersection
common_values_between_two_set = rainbow_colors & favorite_colors

# print(common_values_between_two_set)

# Difference
difference_between_two_set = rainbow_colors ^ favorite_colors
# print(difference_between_two_set)

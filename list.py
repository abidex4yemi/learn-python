# Lists basics

student_score = list([10, 40, 60, 70])

# print(student_score)
# print(type([]))


# make list of names
names = ["Nina", "Max", "Yemi", "Rose"]

# print(type(names))

# print(f"The Total number of names are {len(names)}")
# print(names[2])

###############################
# Changing the order of a list#
###############################

lottery_numbers = [20, 30, 50, 60, 200, 120]

# There are two ways of sorting in python

## First way##
# sorted() function doesn't mutate the list but clone it

sorted_lottery_values = sorted(lottery_numbers)
# print(sorted_lottery_values)

# reverse order
# print(sorted(lottery_numbers, reverse=True))

## Second way of sorting list in python  --in place##
lottery_numbers.sort()
# print(lottery_numbers)

lottery_numbers.reverse()
# print(lottery_numbers)

# print(lottery_numbers.pop())
# print(len(lottery_numbers))

###########################
# Adding items to list  #
###########################

# list
shopping_list = ["Seasoning", "Tomato"]

# add new item to a list
shopping_list.append("Salt")

# add new item to a specific position in list
shopping_list.insert(0, "Oil")

# remove item from a list
del shopping_list[0]
shopping_list.remove("Tomato")

# print(shopping_list)

# combining two list together
my_list_one = [1, 2, 3, 4, 5]
my_list_two = [6, 7, 8, 9, 10]

my_list_one.extend(my_list_two)

# print(my_list_one)


###########################
# List lookups           #
###########################

friend_names = ["Nina", "Ramona", "John", "Nina"]

# check if item exist in list
# print("Nina" in friend_names)

# check item index
# print(friend_names.index("John"))

# check how many time a value exist in a list
# print(friend_names.count("Nina "))

friend_names[0] = "Yemi"

# print(friend_names)

# find item position and change it's value
johnPos = friend_names.index("John")

friend_names[johnPos] = "Jane"

# print(friend_names)

# this will throw an error because specified position does not exist
# friend_names[4] = "Pappy"

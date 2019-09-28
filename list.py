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

print(lottery_numbers.pop())
print(len(lottery_numbers))

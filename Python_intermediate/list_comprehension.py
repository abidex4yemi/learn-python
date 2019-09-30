################################
# Basics of list comprehension #
################################

names = ["Nina", "Max", "Jimmy"]

# print(names[0].lower())
# print(names[1].upper())
# print(names[2].capitalize())

# old way of doing things
upper_names = []
for name in names:
    upper_names.append(name.upper())

# print(upper_names)

# new way of doing things

all_names_in_upper_case = [name.upper() for name in names]
# print(all_names_in_upper_case)

multiplication = [num * num for num in range(6)]
# print(multiplication)

names = ["Tola", "Max", "Yemi", "John"]
length_of_each_name = [("length", len(name)) for name in names]
# print(length_of_each_name)

names = ["Max", "John", "Yemi"]

print(", ".join([f"The name is {name}" for name in names]))

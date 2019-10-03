# slicing in python

my_string = "Hello world!"

# this will show the first character
print(my_string[0])

# this will print the last character
print(my_string[-1])

# this will exclude the last character
print(my_string[:-1])

# this will show the all characters
print(my_string[:])

# this will show the first 4 charaters
print(my_string[:5])

# Note: list are mutable
new_names = []
names = ["Jane", "Doe", "Jane"]

new_names = names
new_names.append("Nina")

print(names)
print(new_names)

new_names = names[:]
new_names.append("Yemi")

print(new_names)

my_string = "Hello world!"
print(my_string[-10:-4])

my_list = list(range(10))
print(my_list[::2])

print(my_list[::-2])
print(my_list)
print(my_list[1:7:2])

###########################
#   Basic type conversion #
##########################

my_data = "This,is,a,comma,seperated,list"
# print(my_data.split(","))

student = "Mary,8,march"
# print(student.split(","))

# Unpacking values from a list
name, age, subject = student.split(",")

# print(name, age, subject)

my_data = "This,is,a,comma,seperated,list"
my_list = my_data.split(",")

# print(my_list)

# join list item to a string
my_data = " ".join(my_list)
# print(my_data)

# print(str("5"))

# print("Today is a good day   " + str(30))

greeting = "Hello"
greeting_in_sequence = list(greeting)
# print(greeting_in_sequence)
# print("".join(greeting_in_sequence))

csv_row = "The,quick,brown,fox"
sentence = csv_row.split(",")
# print(sentence)
# print(" ".join(sentence))

names = ["Nina", "James", "Jane", "Nina"]
unique_names = set(names)
print(unique_names)
print(sorted(unique_names))

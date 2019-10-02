#######################
# Dictionaries basics #
#######################

# Create basic dictionary #

# print(type({}))
# print({})
# print(dict())

numbers = {1: "One", 2: "Two", 3: "Three"}
mix_values = {"1": [10, 4], 2: ("Yemi", "Jane")}
# print(mix_values)


# Accessing the value of a dictionary #
# print(numbers[1])
# print(numbers.get(2))

# if value does not exist this will throw KeyError: '5'
# print(mix_values[2])

# if value does not exist this will none and doesn't throw error
# print(mix_values.get(5))

# setting default value if value does not exist
# print(mix_values.get("Three", "Key does not exist"))


#####################################################
# Adding, Removing, Accessing value in Dictionaries #
#####################################################

students = {"One": "Jane", "Two": "John"}

# Adding #
students["Three"] = "Yemi"
# print(students)

# This will replace existing value
students["Two"] = "New student"
# print(students)

# Using in keyword to check if key exist
# print("One" in students)

# Join two dictionaries together
colors = {"r": "Red", "g": "Green"}
numbers = {"One": 1, "Two": 2, "r": "Red"}
colors.update(numbers)
# print(colors)

vegetables = {"Green": ["Spinach"]}
vegetables["Green"].append("Apples")
# print(vegetables["Green"])

numbers = {"One": 1, "Two": 2, "Three": 3, "Four": 4}
print(numbers.keys())
print(numbers.values())
print(numbers.items())

one, two, three, four = numbers.items()
print(one, two, three, four)

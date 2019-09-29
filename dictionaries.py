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

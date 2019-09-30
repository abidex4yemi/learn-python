##############################################
# Using list comprehension with conditionals #
##############################################

# Basic conditions in list comprehension
even_squares = [num * num for num in range(10) if num % 2 == 0]
# print(even_numbers)

even_squares_in_text = ",".join(
    [f"The square of {int(num / 2)} is {num}" for num in even_squares])

print(even_squares_in_text)

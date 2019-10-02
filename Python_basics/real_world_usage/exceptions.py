################################
# Exception handling in python #
################################

# This will throw error
try:
    int("a")
except ValueError as castingError:
    print(f"Oops can't do this {castingError}")

print("This is the end of the program")

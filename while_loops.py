###########################
# Basic while loops       #
###########################

counter = 0
max_count = 4

while counter < max_count:
    print(f"The count is {counter}")
    counter += 1

names = ["Max", "Rose", "Nina", "Jimmy"]

# Using break keyword
for name in names:
    if name == "Nina":
        break
    print(f"Hello, {name}")

# using continue keyword
for name in names:
    if name == "Nina":
        continue
    print(f"Hello, {name}")

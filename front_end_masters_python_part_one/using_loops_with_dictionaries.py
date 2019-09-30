###########################
# looping over dictionary #
###########################

hex_colors = {"Red": "#FF", "Green": "#008"}

# Getting tuples from dictionaries (index, value)
(firstValue, secondValue) = enumerate(hex_colors)
print(firstValue, secondValue)

# looping and unpacking in dictionaries
for (label, hex_color) in hex_colors.items():
    print(f"The hex value of {label} is {hex_color}")

# using enumerate() to get tuples and unpacking
for (i, color) in enumerate(hex_colors):
    print(f"index: {i}, color: {color}")

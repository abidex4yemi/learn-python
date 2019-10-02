
squares = [num * num for num in range(6)]
print(squares)

sum_of_all_numbers = sum(squares)
print(sum_of_all_numbers)


print(min(squares))
print(max(squares))


print(sorted(squares, reverse=True))

lottery_numbers = "20, 130, 140, 600"
max_lottery_number = max([int(num) for num in lottery_numbers.split(", ")])

print(max_lottery_number)

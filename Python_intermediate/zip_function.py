# Basic zip functions

squares = {num:  num * num for num in range(11)}
print(squares)

print(squares.keys())
print(squares.values())
print(squares.items())


players = ["Yemi", "Jane", "Nina"]
scores = [10, 20, 10]

# joining two list together using zip function
print(zip(players, scores))

print(*zip(players, scores))

print(" ".join([f"Name: {name}, Score: {score}" for name,
                score in zip(players, scores)]))

player_full_details = zip(players, scores)
# convert generator to a list
print(list(player_full_details))

print(dict(zip(players, scores)))

# using generator comprehension

duplicate_names = ["Yemi", "John", "Yemi"]

print(set((name for name in duplicate_names)))

print(set(num * num for num in range(10)))

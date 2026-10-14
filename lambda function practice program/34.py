numbers = [1, 3, 4, 6, 8, 9, 12]
selected = list(filter(lambda x: x % 3 == 0, numbers))
result = list(map(lambda x: x * x * x, selected))
print("Cubes of numbers divisible by 3:", result)

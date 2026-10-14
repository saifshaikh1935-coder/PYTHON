values = input("Enter values separated by spaces: ").split()
result = list(map(lambda value: value.isdigit(), values))
print(result)

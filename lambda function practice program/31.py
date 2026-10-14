from functools import reduce

numbers = [10, 45, 20, 80, 35]
result = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum number:", result)

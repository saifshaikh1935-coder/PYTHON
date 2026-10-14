from functools import reduce

numbers = [10, 45, 20, 80, 35]
result = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum =", result)

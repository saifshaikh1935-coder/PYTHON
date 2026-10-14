from functools import reduce

numbers = [10, 40, 20, 50, 30]
largest = max(numbers)
remaining = list(filter(lambda x: x < largest, numbers))
second_largest = max(remaining)
print("Second-largest number:", second_largest)

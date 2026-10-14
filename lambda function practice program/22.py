numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
result = list(filter(lambda x: x > average, numbers))
print("Average:", average)
print("Numbers greater than average:", result)

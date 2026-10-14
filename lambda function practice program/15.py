numbers = [10, 15, 20, 25, 30, 45, 60]
result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print("Numbers divisible by 3 and 5:", result)

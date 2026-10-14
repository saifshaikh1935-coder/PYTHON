numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
result = list(map(lambda x: x * x, even_numbers))
print("Squares of even numbers:", result)

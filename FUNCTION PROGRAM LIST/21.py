operation = lambda a, b: a * b if isinstance(a, int) and isinstance(b, int) else str(a) + str(b)

first = input("Enter first value: ")
second = input("Enter second value: ")

try:
    first = int(first)
except ValueError:
    pass

try:
    second = int(second)
except ValueError:
    pass

print("Result =", operation(first, second))

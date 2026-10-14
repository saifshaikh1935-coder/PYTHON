def operate(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b, a * b
    return str(a) + str(b), str(a) * int(b)

first = input("Enter first value: ")
second = input("Enter second value: ")

try:
    first = float(first) if "." in first else int(first)
except ValueError:
    pass

try:
    second = float(second) if "." in second else int(second)
except ValueError:
    pass

if isinstance(first, (int, float)) and isinstance(second, (int, float)):
    addition, multiplication = operate(first, second)
    print("Addition =", addition)
    print("Multiplication =", multiplication)
else:
    print("Concatenation =", str(first) + str(second))
    if isinstance(second, int) and second >= 0:
        print("Repetition =", str(first) * second)
    else:
        print("Repetition requires the second value to be a non-negative integer")

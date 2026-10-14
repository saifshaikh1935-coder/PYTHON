factorial = lambda n: 1 if n <= 1 else n * factorial(n - 1)

number = int(input("Enter a non-negative number: "))
if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial =", factorial(number))

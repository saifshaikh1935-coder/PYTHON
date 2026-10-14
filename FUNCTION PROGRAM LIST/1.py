def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def integer_divide(a, b):
    return a // b

def power(a, b):
    return a ** b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Integer Division")
print("6. Power")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    if b != 0:
        print("Result =", divide(a, b))
    else:
        print("Division by zero is not allowed")
elif choice == 5:
    if b != 0:
        print("Result =", integer_divide(a, b))
    else:
        print("Division by zero is not allowed")
elif choice == 6:
    print("Result =", power(a, b))
else:
    print("Invalid choice")

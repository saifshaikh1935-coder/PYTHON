def add(a,b):
    return a+b


def subtract(a,b):
    return a-b


def multiply(a,b):
    return a*b


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def power(a,b):
    return a**b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

choice = int(input("Enter choice: "))

if choice == 1:
    print(add(a,b))
elif choice == 2:
    print(subtract(a,b))
elif choice == 3:
    print(multiply(a,b))
elif choice == 4:
    print(divide(a,b))
elif choice == 5:
    print(power(a,b))

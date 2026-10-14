calculate = lambda number: number * 5 if number % 2 == 0 else number * 10

number = int(input("Enter a number: "))
print("Result =", calculate(number))

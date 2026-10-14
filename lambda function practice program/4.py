n = int(input("Enter a number: "))
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(n))

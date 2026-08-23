def stats(a,b,c):
    total = a+b+c
    average = total/3
    minimum = min(a,b,c)
    maximum = max(a,b,c)

    return total, average, minimum, maximum


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

total, average, minimum, maximum = stats(a,b,c)

print("Sum =", total)
print("Average =", average)
print("Minimum =", minimum)
print("Maximum =", maximum)
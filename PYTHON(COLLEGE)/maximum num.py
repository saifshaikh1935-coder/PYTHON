a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Maximum Number =", a)
elif b >= a and b >= c and b >= d:
    print("Maximum Number =", b)
elif c >= a and c >= b and c >= d:
    print("Maximum Number =", c)
else:
    print("Maximum Number =", d)
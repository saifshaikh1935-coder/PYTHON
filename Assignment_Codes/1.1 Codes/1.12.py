previous = int(input("Enter previous meter reading: "))
current = int(input("Enter current meter reading: "))

units = current-previous
bill = units*5.50+100

print("Units consumed =", units)
print("Total bill =", bill)
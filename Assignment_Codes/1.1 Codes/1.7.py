num = int(input("Enter 3 digit number: "))

hundreds = num//100
tens = (num//10)%10
units = num%10

sum = hundreds+tens+units
product = hundreds*tens*units

print("Hundreds digit =", hundreds)
print("Tens digit =", tens)
print("Units digit =", units)
print("Sum of digits =", sum)
print("Product of digits =", product)
def convert(number):
    return bin(number), oct(number), hex(number)

number = int(input("Enter a decimal number: "))
binary, octal, hexadecimal = convert(number)
print("Binary =", binary)
print("Octal =", octal)
print("Hexadecimal =", hexadecimal)

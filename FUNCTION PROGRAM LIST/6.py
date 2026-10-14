def in_range(number, start, end):
    return start <= number <= end

number = float(input("Enter a number: "))
start = float(input("Enter range start: "))
end = float(input("Enter range end: "))

if in_range(number, start, end):
    print("Number is within the range")
else:
    print("Number is outside the range")

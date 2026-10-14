n = int(input("Enter no: "))
sum = 0
sign = 1

for i in range(1, n+1, 2):
    sum = sum + (sign * i)
    sign = -sign

print(sum)
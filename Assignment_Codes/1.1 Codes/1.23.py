n = int(input("Enter number: "))

sum1 = 0
sum2 = 0
sum3 = 0

for i in range(1,n+1):
    sum1 = sum1+i
    sum2 = sum2+(i**2)
    sum3 = sum3+(i**3)

print("Sum of natural numbers =", sum1)
print("Sum of squares =", sum2)
print("Sum of cubes =", sum3)
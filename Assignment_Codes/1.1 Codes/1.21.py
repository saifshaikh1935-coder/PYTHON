num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp%10
    sum = sum+(digit**3)
    temp = temp//10

if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

print("Armstrong numbers from 1 to 999:")

for num in range(1,1000):
    temp = num
    sum = 0

    while temp > 0:
        digit = temp%10
        sum = sum+(digit**3)
        temp = temp//10

    if num == sum:
        print(num,end=" ")
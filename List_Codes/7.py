list1 = [10,20,10,30,10,40]

num = int(input("Enter number: "))

count = 0

for i in list1:
    if i == num:
        count = count + 1

print("Count =", count)
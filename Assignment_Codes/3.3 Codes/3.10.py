n = int(input("Enter number of elements: "))

list1 = []

for i in range(n):
    list1.append(int(input("Enter number: ")))

print("List =", list1)

unique = set(list1)
print("Without duplicates =", unique)

list2 = [1, 2, 3]

print("List 1 but not List 2 =", set(list1)-set(list2))

count = {}

for num in list1:
    if num in count:
        count[num] = count[num] + 1
    else:
        count[num] = 1

print("Count =", count)
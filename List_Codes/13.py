list1 = [10, 20, 10, 30, 20, 40]

list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print("After removing duplicates =", list2)
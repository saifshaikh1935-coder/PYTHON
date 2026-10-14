list1 = [50, 20, 40, 10, 30]

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print("Ascending =", list1)

list1.reverse()

print("Descending =", list1)
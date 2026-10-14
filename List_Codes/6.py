list1 = [25,10,40,15,60]

maximum = list1[0]
minimum = list1[0]

for i in list1:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Maximum =", maximum)
print("Minimum =", minimum)
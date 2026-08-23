marks = (70, 80, 65, 90, 75)

print("Index 0 =", marks[0])
print("Slicing =", marks[1:4])
print("Length =", len(marks))

a, b, c, d, e = marks
print("Unpacked =", a, b, c, d, e)

minimum = min(marks)
maximum = max(marks)
average = sum(marks)/len(marks)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)

try:
    marks[0] = 100
except TypeError:
    print("TypeError: Tuple cannot be modified")

marks_list = list(marks)
marks_list[0] = 100
marks = tuple(marks_list)

print("Modified tuple =", marks)
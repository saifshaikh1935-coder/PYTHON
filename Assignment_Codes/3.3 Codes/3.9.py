gradebook = {
    "SHARIF": [80, 75, 90],
    "SAHIL": [70, 85, 80],
    "ASAD": [90, 95, 88]
}

average = {}

for student in gradebook:
    average[student] = sum(gradebook[student])/3

sorted_students = sorted(average.items(), key=lambda x: x[1], reverse=True)

for student, avg in sorted_students:
    print(student, ":", avg)

print("Top student =", sorted_students[0][0])
students = [
    ("Faiz", 75),
    ("Asad", 55),
    ("Sahil", 90),
    ("Sharif", 65),
    ("Taha", 45)
]

students.sort(key=lambda x: x[1], reverse=True)

print("Sorted students:")

for student in students:
    print(student)

passed = list(filter(lambda x: x[1] >= 60, students))

print("Students with marks >= 60:")

for student in passed:
    print(student)
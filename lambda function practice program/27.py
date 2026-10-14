students = [
    {"name": "Aman", "marks": 75},
    {"name": "Riya", "marks": 92},
    {"name": "Neha", "marks": 85}
]
result = sorted(students, key=lambda x: x["marks"])
print("Students sorted by marks:", result)

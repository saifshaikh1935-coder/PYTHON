employees = [
    ("Aman", "IT", 60000),
    ("Riya", "HR", 55000),
    ("Neha", "IT", 70000),
    ("Jay", "IT", 45000)
]
result = list(filter(lambda x: x[1] == "IT" and x[2] > 50000, employees))
print("IT employees with salary above 50000:", result)

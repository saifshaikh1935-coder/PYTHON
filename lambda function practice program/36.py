students = [("Aman", 75), ("Riya", 35), ("Neha", 85), ("Jay", 28), ("Zara", 60)]
passed = list(filter(lambda x: x[1] >= 40, students))
result = sorted(passed, key=lambda x: x[1])
print("Passed students sorted by marks:", result)

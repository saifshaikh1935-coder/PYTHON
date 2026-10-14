students = [("Aman", 75), ("Riya", 92), ("Neha", 85), ("Jay", 68), ("Zara", 95)]
result = sorted(students, key=lambda x: x[1], reverse=True)
print("Top 3 students:", result[:3])

students = [("Aman", 75), ("Riya", 92), ("Neha", 85), ("Jay", 68), ("Zara", 95)]
ranking = sorted(students, key=lambda x: x[1], reverse=True)
print("Student ranking:")
for rank, student in enumerate(ranking, start=1):
    print(rank, student[0], student[1])

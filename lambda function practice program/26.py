employees = [("Aman", 35000), ("Riya", 50000), ("Neha", 42000), ("Jay", 30000)]
result = sorted(employees, key=lambda x: x[1])
print("Employees sorted by salary:", result)

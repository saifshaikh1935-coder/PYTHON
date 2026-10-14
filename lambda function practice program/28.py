employees = [
    {"name": "Aman", "salary": 45000},
    {"name": "Riya", "salary": 65000},
    {"name": "Neha", "salary": 55000},
    {"name": "Jay", "salary": 40000}
]
result = list(filter(lambda x: x["salary"] > 50000, employees))
print("Employees with salary above 50000:", result)

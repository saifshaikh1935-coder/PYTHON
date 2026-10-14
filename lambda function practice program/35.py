salaries = [30000, 45000, 50000, 60000, 75000]
selected = list(filter(lambda x: x > 40000, salaries))
result = list(map(lambda x: x * 1.10, selected))
print("Increased salaries:", result)

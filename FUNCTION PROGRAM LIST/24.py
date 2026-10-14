students = ["Amit", "Bina", "Christopher", "Neha", "Rahul", "Jay"]
result = list(filter(lambda name: len(name) < 6, students))
print("Students with names less than 6 characters:", result)

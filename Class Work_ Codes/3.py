students = {
    101: {
        "Name": "Saif",
        "Age": 19,
        "Course": "BSc IT",
        "Semester": 3,
        "City": "Ahmedabad",
        "Phone": "9876543210",
        "Subjects": {
            "Python": 80,
            "PHP": 75
        }
    }
}

roll = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
semester = int(input("Enter Semester: "))
city = input("Enter City: ")
phone = input("Enter Phone: ")

students[roll] = {
    "Name": name,
    "Age": age,
    "Course": course,
    "Semester": semester,
    "City": city,
    "Phone": phone,
    "Subjects": {}
}

print("Student added successfully")
print(students)
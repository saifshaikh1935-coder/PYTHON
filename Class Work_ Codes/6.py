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

if roll in students:
    city = input("Enter New City: ")
    phone = input("Enter New Phone: ")

    students[roll].update({
        "City": city,
        "Phone": phone
    })

    print("Details updated successfully")
    print(students[roll])
else:
    print("Student not found")
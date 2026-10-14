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

    subject = input("Enter Subject: ")
    marks = int(input("Enter Marks: "))

    students[roll]["Subjects"][subject] = marks

    print("Subject added successfully")
    print(students[roll]["Subjects"])

else:
    print("Student not found")
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

    print("Name:", students[roll]["Name"])

    for subject, marks in students[roll]["Subjects"].items():
        print("Subject:", subject)
        print("Marks:", marks)

else:
    print("Student not found")
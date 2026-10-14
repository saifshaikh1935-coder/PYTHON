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

    if subject in students[roll]["Subjects"]:
        students[roll]["Subjects"].pop(subject)
        print("Subject removed successfully")
    else:
        print("Subject not found")

else:
    print("Student not found")

print(students[roll])
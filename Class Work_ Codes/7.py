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
    },

    102: {
        "Name": "Rahul",
        "Age": 19,
        "Course": "BSc IT",
        "Semester": 3,
        "City": "Ahmedabad",
        "Phone": "9876543211",
        "Subjects": {
            "Python": 70,
            "PHP": 78
        }
    }
}

roll = int(input("Enter Roll Number: "))

if roll in students:
    students.pop(roll)
    print("Student deleted successfully")
else:
    print("Student not found")

print(students)
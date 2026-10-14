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

for roll, student in students.items():
    print("Roll Number:", roll)
    print("Name:", student["Name"])
    print("Age:", student["Age"])
    print("Course:", student["Course"])
    print("Semester:", student["Semester"])
    print("City:", student["City"])
    print("Phone:", student["Phone"])
    print("Subjects:", student["Subjects"])
    print("----------------------")
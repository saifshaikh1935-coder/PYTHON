student_name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))

marks_5_subjects = []

for i in range(5):
    marks = int(input("Enter marks: "))
    marks_5_subjects.append(marks)

total = sum(marks_5_subjects)
percentage = total/5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "Fail"

print(f"{'Student Name':<15}: {student_name}")
print(f"{'Roll No':<15}: {roll_no}")
print(f"{'Total':<15}: {total}")
print(f"{'Percentage':<15}: {percentage}")
print(f"{'Grade':<15}: {grade}")
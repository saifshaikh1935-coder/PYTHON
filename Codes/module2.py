def employee(emp_id, name, salary, join_date, ch):
    match ch:
        case 1:
            print("Employee ID :", emp_id)
            print("Employee Name :", name)
            print("Salary :", salary)
            print("Join Date :", join_date)

        case 2:
            print("Exit")

        case _:
            print("Invalid Choice")


emp_id = int(input("Enter Employee ID : "))
name = input("Enter Employee Name : ")
salary = float(input("Enter Salary : "))
join_date = input("Enter Join Date : ")

print("1. Display Employee Details")
print("2. Exit")

ch = int(input("Enter Choice : "))

employee(emp_id, name, salary, join_date, ch)
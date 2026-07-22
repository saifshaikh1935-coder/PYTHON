age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))

if age >= 21 and salary >= 25000:
    print("Loan Approved")
elif age >= 21 and salary < 25000:
    print("Salary is too low")
else:
    print("Not Eligible")
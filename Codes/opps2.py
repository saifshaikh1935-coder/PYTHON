class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate(self):

        if self.salary <= 15000:
            hr = self.salary * 0.10
            da = self.salary * 0.20
            pf = self.salary * 0.12

        elif self.salary <= 30000:
            hr = self.salary * 0.15
            da = self.salary * 0.25
            pf = self.salary * 0.12

        else:
            hr = self.salary * 0.20
            da = self.salary * 0.30
            pf = self.salary * 0.12

        gross_salary = self.salary + hr + da
        net_salary = gross_salary - pf

        print("Name:", self.name)
        print("Basic Salary:", self.salary)
        print("HR:", hr)
        print("DA:", da)
        print("PF:", pf)
        print("Gross Salary:", gross_salary)
        print("Net Salary:", net_salary)


name = input("Enter Employee Name: ")
salary = float(input("Enter Basic Salary: "))

e = Employee(name, salary)
e.calculate()
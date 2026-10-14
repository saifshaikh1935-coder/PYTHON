class Student:
    def __init__(self):
        self.name = ""
        self.rollno = 0
        self.age = 0
        self.marks = []

    def getData(self):
        self.name = input("Enter Name: ")
        self.rollno = int(input("Enter Roll No: "))
        self.age = int(input("Enter Age: "))

        for i in range(3):
            mark = float(input("Enter marks of subject " + str(i + 1) + ": "))
            self.marks.append(mark)

    def calculate(self):
        total = sum(self.marks)
        percentage = total / 3

        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Total:", total)
        print("Percentage:", percentage, "%")


s = Student()
s.getData()
s.calculate()
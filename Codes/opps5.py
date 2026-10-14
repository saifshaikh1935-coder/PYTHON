class Student:
    def get_student(self):
        self.name = input("Enter Student Name: ")
        self.rno = int(input("Enter Roll No: "))
        self.sem = int(input("Enter Semester: "))
        self.div = input("Enter Division: ")

    def display_student(self):
        print("\n--- Student Details ---")
        print("Name       :", self.name)
        print("Roll No    :", self.rno)
        print("Semester   :", self.sem)
        print("Division   :", self.div)


class InternalExam(Student):
    def get_internal(self):
        print("\nEnter Internal Marks (3 Subjects)")
        self.i1 = float(input("Subject 1: "))
        self.i2 = float(input("Subject 2: "))
        self.i3 = float(input("Subject 3: "))

        self.itotal = self.i1 + self.i2 + self.i3
        self.iavg = self.itotal / 3
        self.imax = max(self.i1, self.i2, self.i3)

    def display_internal(self):
        print("\n--- Internal Exam ---")
        print("Subject 1 :", self.i1)
        print("Subject 2 :", self.i2)
        print("Subject 3 :", self.i3)
        print("Total     :", self.itotal)
        print("Average   :", self.iavg)
        print("Maximum   :", self.imax)


class ExternalExam(Student):
    def get_external(self):
        print("\nEnter External Marks (3 Subjects)")
        self.e1 = float(input("Subject 1: "))
        self.e2 = float(input("Subject 2: "))
        self.e3 = float(input("Subject 3: "))

        self.etotal = self.e1 + self.e2 + self.e3
        self.eavg = self.etotal / 3
        self.emax = max(self.e1, self.e2, self.e3)

    def display_external(self):
        print("\n--- External Exam ---")
        print("Subject 1 :", self.e1)
        print("Subject 2 :", self.e2)
        print("Subject 3 :", self.e3)
        print("Total     :", self.etotal)
        print("Average   :", self.eavg)
        print("Maximum   :", self.emax)


s1 = InternalExam()
s2 = ExternalExam()

print("===== STUDENT DETAILS =====")
s1.get_student()

s2.name = s1.name
s2.rno = s1.rno
s2.sem = s1.sem
s2.div = s1.div

print("\n===== INTERNAL EXAM =====")
s1.get_internal()
s1.display_student()
s1.display_internal()

print("\n===== EXTERNAL EXAM =====")
s2.get_external()
s2.display_student()
s2.display_external()
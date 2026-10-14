
# 1. SINGLE INHERITANCE
# Parent Class
class ABC:
    def getData(self):
        self.x = 10
        self.y = 20

    def display(self):
        print("X =", self.x)
        print("Y =", self.y)


# Child Class
class XYZ(ABC):
    def show(self):
        print("This is Single Inheritance")


x1 = XYZ()
x1.getData()
x1.display()
x1.show()


# --------------------------------------------------
# 2. MULTILEVEL INHERITANCE
# --------------------------------------------------

class A:
    def getA(self):
        self.a = 10


class B(A):
    def getB(self):
        self.b = 20


class C(B):
    def getC(self):
        self.c = 30

    def display(self):
        print("A =", self.a)
        print("B =", self.b)
        print("C =", self.c)


obj = C()
obj.getA()
obj.getB()
obj.getC()
obj.display()


# --------------------------------------------------
# 3. MULTIPLE INHERITANCE
# --------------------------------------------------

class P:
    def getP(self):
        self.p = 100


class Q:
    def getQ(self):
        self.q = 200


class R(P, Q):
    def display(self):
        print("P =", self.p)
        print("Q =", self.q)


obj = R()
obj.getP()
obj.getQ()
obj.display()


# --------------------------------------------------
# 4. HIERARCHICAL INHERITANCE
# --------------------------------------------------

class Parent:
    def getData(self):
        self.x = 50

    def display(self):
        print("X =", self.x)


class Child1(Parent):
    def show1(self):
        print("Child 1")


class Child2(Parent):
    def show2(self):
        print("Child 2")


obj1 = Child1()
obj1.getData()
obj1.display()
obj1.show1()

obj2 = Child2()
obj2.getData()
obj2.display()
obj2.show2()


# --------------------------------------------------
# 5. METHOD OVERRIDING
# --------------------------------------------------

class ABC1:
    def getData(self):
        self.x = 10
        self.y = 20
        self.z = 30
        self.p = 0


class XYZ1(ABC1):
    def getData(self):
        self.z = 50
        self.y = 70
        self.p = 30


x1 = ABC1()
x1.getData()

print("Parent Class:")
print(x1.y)
print(x1.z)
print(x1.p)


x2 = XYZ1()
x2.getData()

print("Child Class:")
print(x2.y)
print(x2.z)
print(x2.p)


# --------------------------------------------------
# 6. HYBRID INHERITANCE
# --------------------------------------------------

class H1:
    def getH1(self):
        self.h1 = 10


class H2(H1):
    def getH2(self):
        self.h2 = 20


class H3(H1):
    def getH3(self):
        self.h3 = 30


class H4(H2, H3):
    def display(self):
        print("H1 =", self.h1)
        print("H2 =", self.h2)
        print("H3 =", self.h3)


obj = H4()

obj.getH1()
obj.getH2()
obj.getH3()

obj.display()

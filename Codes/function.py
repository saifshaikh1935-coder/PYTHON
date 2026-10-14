# Addition

def addition(a,b):
    c=a+b
    return c

x=int(input("Enter value 1 "))
y=int(input("Enter value 2 "))

z=addition(x,y)

print("ans is ",z)


# Multiple return values

def calculation(a,b):
    return a+b,a-b,a*b

x=int(input("Enter value 1 "))
y=int(input("Enter value 2 "))

z=calculation(x,y)

print("ans is ",z)

p,q,r=calculation(x,y)

print(p,q,r)
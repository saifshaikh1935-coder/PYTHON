def interest(p, r, t, ch):
    match ch:
        case 1:
            si = (p * r * t) / 100
            print("Simple Interest =", si)

        case 2:
            ci = p * (1 + r / 100) ** t - p
            print("Compound Interest =", ci)

        case _:
            print("Invalid Choice")


p = float(input("Enter Principal : "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))

print("1. Simple Interest")
print("2. Compound Interest")

ch = int(input("Enter Choice : "))

interest(p, r, t, ch)
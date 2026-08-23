n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter number: "))
    a.append(x)

print("List =", a)
print("Sorted list =", sorted(a))
print("Reversed list =", a[::-1])
print("Maximum =", max(a))
print("Minimum =", min(a))
print("Sum =", sum(a))
print("Average =", sum(a)/n)
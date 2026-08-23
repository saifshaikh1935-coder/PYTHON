set1 = set(range(1,16,2))
set2 = set(range(3,16,3))

print("Set 1 =", set1)
print("Set 2 =", set2)

print("Union =", set1 | set2)
print("Intersection =", set1 & set2)
print("Difference set1-set2 =", set1 - set2)
print("Difference set2-set1 =", set2 - set1)
print("Symmetric Difference =", set1 ^ set2)
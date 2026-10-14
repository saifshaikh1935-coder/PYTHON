numbers = [5, 2, 5, 3, 2, 8, 1, 3]
seen = []
unique = list(filter(lambda x: x not in seen and not seen.append(x), numbers))
result = sorted(unique)
print("Unique numbers in sorted order:", result)

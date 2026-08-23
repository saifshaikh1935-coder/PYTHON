matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row[0], row[1], row[2])

for row in matrix:
    print("Row sum =", sum(row))

diagonal = matrix[0][0] + matrix[1][1] + matrix[2][2]

print("Main diagonal sum =", diagonal)
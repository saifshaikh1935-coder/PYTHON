matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = lambda matrix: [list(row) for row in zip(*matrix)]
print(transpose(matrix))

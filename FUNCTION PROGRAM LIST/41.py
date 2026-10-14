def sort_matrix(M):
    return sorted(M, key=lambda row: row)

M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(sort_matrix(M))

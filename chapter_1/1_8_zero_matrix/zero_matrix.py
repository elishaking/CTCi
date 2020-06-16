def zero_matrix(matrix: list):
    N = len(matrix)
    M = len(matrix[0])
    zero_rows = {}
    zero_cols = {}

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True

    for key in zero_rows.keys():
        for j in range(M):
            matrix[key][j] = 0

    for key in zero_cols.keys():
        for i in range(N):
            matrix[i][key] = 0

    return matrix


print(zero_matrix([[1, 2, 0], [2, 0, 7], [1, 4, 3]]))

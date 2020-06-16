def rotate_matrix(image: list):
    rotated = []
    N = len(image)
    for i in range(N):
        rotated.append([])
        for j in range(N):
            rotated[i].append(image[j][N-i-1])

    return rotated


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

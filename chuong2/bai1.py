def mang_doi_xung(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Kiểm tra kết quả
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if mang_doi_xung(matrix):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")

def mang_tam_giac_tren(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Chỉ cần kiểm tra phần tử trên đường chéo phía trên
            if matrix[i][j] != 0:
                return False
    return True

# Kiểm tra kết quả
matrix = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

if mang_tam_giac_tren(matrix):
    print("Ma trận là ma trận tam giác trên.")
else:
    print("Ma trận không phải là ma trận tam giác trên.")

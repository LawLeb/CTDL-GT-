def mang_trung_hang(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i] == matrix[j]:
                return True
    return False

# Kiểm tra kết quả
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

if mang_trung_hang(matrix):
    print("Ma trận có ít nhất hai hàng giống nhau.")
else:
    print("Ma trận không có hai hàng giống nhau.")

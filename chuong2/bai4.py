def mang_nhom_hang(matrix):
    n = len(matrix)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            group_indices = [i]
            visited[i] = True
            for j in range(i + 1, n):
                if matrix[i] == matrix[j]:
                    group_indices.append(j)
                    visited[j] = True
            print("Nhóm chỉ mục hàng:", group_indices)

# Kiểm tra kết quả
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 8, 9]
]

print("Các nhóm chỉ mục hàng giống nhau:")
mang_nhom_hang(matrix)

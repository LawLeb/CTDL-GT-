def pascal_triangle(n):
    for line in range(0, n):
        # In khoảng trắng để căn lề
        for _ in range(0, n - line - 1):
            print(" ", end="")
        # Tính toán và in ra các số trên mỗi hàng của tam giác Pascal
        for i in range(0, line + 1):
            print(binomial_coefficient(line, i), " ", end="")
        print()

def binomial_coefficient(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res


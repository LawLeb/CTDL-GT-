def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def neper(n):
    e = 0
    for k in range(n+1):
        e += 1 / factorial(k)
    return e

# Kiểm tra kết quả
n = int(input("Nhập số nguyên n >= 0: "))
print("Số e (tổng a0 + a1 + ... + an) là:", neper(n))

# giải thuật đệ qui
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Nhập số nguyên n >= 0: "))
print("Số Fibonacci thứ", n, "là:", fibonacci_recursive(n))

# giải thuật không đệ qui
def fibonacci_non_recursive(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            c = a + b
            a, b = b, c
        return b

# Kiểm tra kết quả
n = int(input("Nhập số nguyên n >= 0: "))
print("Số Fibonacci thứ", n, "là:", fibonacci_non_recursive(n))

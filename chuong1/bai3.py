# giải thuật đệ qui
def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)

# Kiểm tra kết quả
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
print("Ước số chung lớn nhất của", m, "và", n, "là:", gcd_recursive(m, n))

# giải thuật không đệ qui
def gcd_non_recursive(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# Kiểm tra kết quả
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
print("Ước số chung lớn nhất của", m, "và", n, "là:", gcd_non_recursive(m, n))

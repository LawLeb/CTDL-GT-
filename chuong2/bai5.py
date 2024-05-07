def cong(a, b):
    # Đảo ngược mảng để thực hiện phép cộng từ hàng đơn vị lên
    a = a[::-1]
    b = b[::-1]

    result = []
    carry = 0
    max_length = max(len(a), len(b))

    for i in range(max_length):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0

        sum_digit = digit_a + digit_b + carry
        result.append(sum_digit % 10)
        carry = sum_digit // 10

    if carry > 0:
        return [-1] * (max_length + 1)  # Kết quả bị tràn
    else:
        return result[::-1]  # Đảo ngược mảng để đưa về dạng đúng

# Kiểm tra kết quả
a = [1, 2, 3]  # Số 123
b = [9, 8, 7]  # Số 987
print("Kết quả của a + b:", cong(a, b))

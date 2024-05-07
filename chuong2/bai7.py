def nhan(a, b):
    # Đảo ngược mảng để thực hiện phép nhân từ hàng đơn vị lên
    a = a[::-1]
    b = b[::-1]

    result = [0] * (len(a) + len(b))  # Khởi tạo mảng kết quả

    for i in range(len(a)):
        carry = 0
        for j in range(len(b)):
            # Thực hiện phép nhân từng chữ số và cộng vào kết quả tạm thời
            temp = result[i + j] + a[i] * b[j] + carry
            result[i + j] = temp % 10
            carry = temp // 10

        # Cộng số dư vào vị trí tiếp theo
        result[i + len(b)] += carry

    # Loại bỏ các số 0 dư ở đầu
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Kiểm tra kết quả có bị tràn không
    if len(result) > len(a) + len(b):
        return [-1]  # Kết quả bị tràn
    else:
        return result[::-1]  # Đảo ngược mảng để đưa về dạng đúng

print("Kết quả của a × b:", nhan(a, b))

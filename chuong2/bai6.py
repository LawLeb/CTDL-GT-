def tru(a, b):
    # Đảo ngược mảng để thực hiện phép trừ từ hàng đơn vị lên
    a = a[::-1]
    b = b[::-1]

    result = []
    borrow = 0

    for i in range(len(b)):
        digit_a = int(a[i]) - borrow
        digit_b = int(b[i])

        if digit_a < digit_b:
            digit_a += 10
            borrow = 1
        else:
            borrow = 0

        result.append(digit_a - digit_b)

    for i in range(len(b), len(a)):
        digit_a = int(a[i]) - borrow

        if digit_a < 0:
            digit_a += 10
            borrow = 1
        else:
            borrow = 0

        result.append(digit_a)

    # Loại bỏ các số 0 dư ở đầu
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result[::-1]  # Đảo ngược mảng để đưa về dạng đúng

# Kiểm tra kết quả
a = [7, 5, 8, 2]  # Số 7582
b = [3, 9, 1]     # Số 391
print("Kết quả của a - b:", tru(a, b))

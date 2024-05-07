def Duynhat(a):
    unique_numbers = sorted(set(a))
    return unique_numbers

# Test
arr_a = [1, 5, 3, 7, 5, 9, 7]
arr_b = Duynhat(arr_a)
print("Mảng b sau khi trích xuất các số duy nhất và sắp xếp tăng dần:", arr_b)  # Kết quả: [1, 3, 5, 7, 9]

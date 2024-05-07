def Hieu(a, b):
    set_a = set(a)
    set_b = set(b)
    difference_set = set_a.difference(set_b)
    sorted_difference = sorted(difference_set)
    return sorted_difference

# Test
arr_a = [1, 5, 3, 7, 9, 4, 2]
arr_b = [9, 6, 2, 3, 8]
arr_c = Hieu(arr_a, arr_b)
print("Mảng c chứa các số duy nhất trong a mà không có trong b:", arr_c)  # Kết quả: [1, 4, 5, 7]

def Giao(a, b):
    set_a = set(a)
    set_b = set(b)
    intersection_set = set_a.intersection(set_b)
    sorted_intersection = sorted(intersection_set)
    return sorted_intersection

# Test
arr_a = [1, 5, 3, 7, 9, 4, 2]
arr_b = [9, 6, 2, 3, 8]
arr_c = Giao(arr_a, arr_b)
print("Mảng c chứa các số duy nhất trong cả a và b:", arr_c)  # Kết quả: [2, 3, 9]

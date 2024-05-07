def Hop(a, b):
    set_a = set(a)
    set_b = set(b)
    union_set = set_a.union(set_b)
    sorted_union = sorted(union_set)
    return sorted_union

# Test
arr_a = [1, 5, 3, 7, 9, 4, 2]
arr_b = [9, 6, 2, 3, 8]
arr_c = Hop(arr_a, arr_b)
print("Mảng c chứa các số duy nhất trong cả a và b:", arr_c)  # Kết quả: [1, 2, 3, 4, 5, 6, 7, 8, 9]

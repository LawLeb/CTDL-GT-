def classify_number(n):
    sum_of_divisors = sum([i for i in range(1, n) if n % i == 0])
    if sum_of_divisors < n:
        return "deficient"
    elif sum_of_divisors == n:
        return "perfect"
    else:
        return "abundant"

def number(x, y):
    for num in range(x, y+1):
        classification = classify_number(num)
        print("Số", num, "là", classification)


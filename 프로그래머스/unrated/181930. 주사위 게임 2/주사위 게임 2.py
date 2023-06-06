def solution(a, b, c):
    diff_nums = len(set([a,b,c]))
    base_sum = sum([a,b,c])
    if diff_nums == 3: return base_sum
    elif diff_nums == 2: return base_sum * (a ** 2 + b ** 2 + c ** 2)
    else: return base_sum * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
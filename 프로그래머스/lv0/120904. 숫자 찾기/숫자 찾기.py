def solution(num, k):
    for idx, n in enumerate(str(num)):
        if str(k) == n: return idx + 1
    return -1
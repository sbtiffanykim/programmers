def solution(array):
    max_n = max(array)
    max_idx = array.index(max_n)
    return [max_n, max_idx]
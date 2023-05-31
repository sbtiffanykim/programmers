from itertools import combinations

def solution(numbers):
    answer = []
    two_nums = list(combinations(numbers, 2))
    answer = [sum(n) for n in two_nums]
    answer = list(set(answer))
    answer.sort()
    return answer
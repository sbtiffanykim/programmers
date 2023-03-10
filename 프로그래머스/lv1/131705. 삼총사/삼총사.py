from itertools import combinations

def solution(number):
    answer = 0
    cases = list(combinations(number, 3))
    for c in cases:
        if sum(c) == 0: answer += 1
    return answer
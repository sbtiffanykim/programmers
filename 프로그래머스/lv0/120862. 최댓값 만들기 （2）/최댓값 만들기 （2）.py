from itertools import combinations
from operator import mul

def solution(numbers):
    answer = -10e8
    num_list = list(combinations(numbers, 2))
    for n in num_list:
        temp = mul(n[0], n[1])
        if temp > answer:
            answer = temp
    return answer
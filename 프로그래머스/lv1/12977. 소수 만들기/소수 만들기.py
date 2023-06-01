from math import sqrt
from itertools import combinations

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    num_prob = [sum(c) for c in combi]
    for num in num_prob:
        if is_prime(num): answer += 1
    return answer
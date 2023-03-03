import math

def solution(box, n):
    answer = 0
    a = [l//n for l in box]
    answer = math.prod(a)
    return answer
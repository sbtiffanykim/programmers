import math

def divisor(num):
    cnt = 1
    for k in range(2, int(math.sqrt(num))+1):
        if num % k == 0:
            cnt += 1
    cnt *= 2
    if math.sqrt(num) ** 2 == num: cnt -= 1
    return cnt
            

def solution(n):
    answer = 0
    for i in range(4, n+1):
        if divisor(i) > 2:
            answer += 1
    return answer
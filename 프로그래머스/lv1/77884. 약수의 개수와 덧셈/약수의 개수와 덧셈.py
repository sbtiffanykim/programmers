from math import sqrt

def num_div(n):
    cnt = 2 # 1 and itself
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: cnt += 2
        if i ** 2 == n: cnt -= 1
    return 1 if cnt % 2 == 0 else 0
        

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        # if the num == 1
        if i == 1: answer -= 1
        
        else:
            if num_div(i): answer += i
            else: answer -= i
        
    return answer
from math import sqrt

def solution(n):
    answer = 0
    
    if n < 2: return n
            
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if i ** 2 == n:
                answer += i
            else:
                answer += i
                answer += (n // i)
    
    return answer
from math import sqrt

def get_prime_num(n):
    for t in range(2, int(sqrt(n)+1)):
        if n % t == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if get_prime_num(i): 
            answer += 1
        
    return answer
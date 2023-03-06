import math

def is_prime_num(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1

def solution(n):
    answer = []
    
    # divisors
    div_list = [i for i in range(2, n+1) if n % i == 0]
    # evaluate whether a given divisor of n is prime number or not
    for div in div_list:
        pm = is_prime_num(div)
        if pm == 1: answer.append(div)
    return answer
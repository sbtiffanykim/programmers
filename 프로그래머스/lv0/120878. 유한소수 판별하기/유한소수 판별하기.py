from math import gcd

def solution(a, b):
    denom = b // gcd(a, b)
    while denom % 2 == 0:
        denom //= 2
    while denom % 5 == 0:
        denom //= 5
    
    return 1 if denom == 1 else 2
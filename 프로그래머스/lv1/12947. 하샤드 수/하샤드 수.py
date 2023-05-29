def solution(x):
    sums = 0
    n = x
    while n >= 1:
        sums += n % 10
        n //= 10
    
    return True if x % sums == 0 else False
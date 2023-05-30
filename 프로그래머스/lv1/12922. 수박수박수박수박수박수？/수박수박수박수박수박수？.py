def solution(n):
    base = '수박'
    
    if n % 2 == 0:
        return base * (n // 2)
    else:
        return base * (n // 2) + base[0]
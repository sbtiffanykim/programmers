def solution(a, b):
    answer = 0
    
    if a == b: return a
    elif a > b:
        a, b = b, a
    
    return sum([n for n in range(a, b+1)])
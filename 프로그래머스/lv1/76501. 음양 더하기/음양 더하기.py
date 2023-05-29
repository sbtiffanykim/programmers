def solution(absolutes, signs):
    answer = 0
    
    for a, s in zip(absolutes, signs):
        if s == False: a *= -1
        answer += a
    
    return answer
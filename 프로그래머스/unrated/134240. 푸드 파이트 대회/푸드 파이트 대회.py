def solution(food):
    answer = ''
    
    for idx, num in enumerate(food):
        if num == 1:
            pass
        else:
            answer += str(idx) * (num // 2)
    answer = answer + '0' + answer[::-1]
    
    return answer
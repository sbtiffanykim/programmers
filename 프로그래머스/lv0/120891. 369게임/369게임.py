def solution(order):
    answer = 0
    for val in str(order):
        if int(val) % 3 == 0 and int(val) != 0: answer += 1
    
    return answer
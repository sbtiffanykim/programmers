def solution(arr, divisor):
    answer = []
    
    answer = list(filter(lambda x: x % divisor == 0, arr))
    answer.sort()
    if len(answer) == 0: answer.append(-1)
    
    return answer
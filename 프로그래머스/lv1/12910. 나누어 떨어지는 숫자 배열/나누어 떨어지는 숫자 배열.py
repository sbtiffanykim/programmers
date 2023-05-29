def solution(arr, divisor):
    answer = []
    
    answer = list(filter(lambda x: x % divisor == 0, arr))
    answer.sort()
    
    return answer if len(answer) != 0 else [-1]
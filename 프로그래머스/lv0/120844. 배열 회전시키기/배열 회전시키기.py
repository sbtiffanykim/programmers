def solution(numbers, direction):
    answer = [0] * len(numbers)
    if direction == "right":
        for i in range(len(numbers)):
            try:
                answer[i+1] = numbers[i]
            except IndexError:
                answer[0] = numbers[i]
    else:
        for i in range(len(numbers)):
            try:
                answer[i-1] = numbers[i]
            except IndexError:
                answer[len(numbers)-1] = numbers[i]
    
    return answer
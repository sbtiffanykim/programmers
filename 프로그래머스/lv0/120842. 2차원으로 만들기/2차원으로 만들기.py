def solution(num_list, n):
    answer = []
    temp = []
    for idx, num in enumerate(num_list, start = 1):
        temp.append(num)
        if idx % n == 0:
            answer.append(temp)
            temp = []
    if len(temp) > 0:
        answer.append(temp)
    return answer
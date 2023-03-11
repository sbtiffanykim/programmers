def solution(my_str, n):
    answer = []
    for idx in range(0, len(my_str), n):
        try:
            answer.append(my_str[idx:idx+n])
        except:
            answer.append(my_str[idx:])
    return answer
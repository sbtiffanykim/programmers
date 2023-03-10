def solution(my_string):
    p = list(my_string.lower())
    p.sort()
    answer = ''.join(p)
    return answer
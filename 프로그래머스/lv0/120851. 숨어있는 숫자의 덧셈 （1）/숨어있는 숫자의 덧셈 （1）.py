def solution(my_string):
    answer = 0
    for char in my_string:
        if ord(char) in range(48, 58):
            answer += int(char)
    return answer
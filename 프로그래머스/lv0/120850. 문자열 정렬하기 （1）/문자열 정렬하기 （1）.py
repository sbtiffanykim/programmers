def solution(my_string):
    answer = []
    for char in my_string:
        if ord(char) in range(48, 58):
            answer.append(int(char))
    answer.sort()
    return answer
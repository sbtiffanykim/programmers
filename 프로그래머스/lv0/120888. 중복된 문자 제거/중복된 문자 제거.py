def solution(my_string):
    stack = []
    for char in my_string:
        if char not in stack:
            stack.append(char)
    answer = ''.join(stack)
    return answer